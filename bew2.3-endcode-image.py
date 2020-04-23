from PIL import Image 

# merge_rbg function got from https://github.com/kelvins/steganography/blob/master/steganography.py
def merge_rgb(rgb1, rgb2):
        r1, g1, b1 = rgb1
        r2, g2, b2 = rgb2
        rgb = (r1[:4] + r2[:4],
               g1[:4] + g2[:4],
               b1[:4] + b2[:4])
        return rgb

# To encode image; hide image within an image
def encode_img(file_location, file_location2):

    img1 = Image.open(file_location)
    img2 = Image.open(file_location2)

    pixels_image1 = img1.load()
    pixels_image2 = img2.load()

    mixed_image = Image.new(img1.mode, img1.size)
    pixels_mixed_image = mixed_image.load()


    for i in range(img1.size[0]): # width
        for j in range(img1.size[1]): # height
            pixel_map1 = pixels_image1[i, j]
            (r, g, b) = bin(pixel_map1[0]), bin(pixel_map1[1]), bin(pixel_map1[2])
            r = r.replace("0b", "")
            b = b.replace("0b", "")
            g = g.replace("0b", "")
            rgb1 = (r, g, b)
            # print(rbg1)

            (r2, g2, b2) = bin(0), bin(0), bin(0)
            r2 = r2.replace("0b", "")
            b2 = b2.replace("0b", "")
            g2 = g2.replace("0b", "")
            rgb2 = (r2, g2, b2)
            # print(rbg2)

            pixel_map2 = pixels_image2[i, j]
            if i < img2.size[0] and j < img2.size[1]:
                (r2, g2, b2) = bin(pixel_map1[0]), bin(pixel_map1[1]), bin(pixel_map1[2])
                r2 = r2.replace("0b", "")
                b2 = b2.replace("0b", "")
                g2 = g2.replace("0b", "")
                rgb2 = (r2, g2, b2)

            rgb = merge_rgb(rgb1, rgb2)

            r, g, b = rgb

            pixels_mixed_image[i, j] = (int(r, 2), int(g, 2), int(b, 2))

    mixed_image.save("newImage.png")

encode_img("encoded_sample.png", "decoded_image.png")


# To decode hidden stuff from image
def decode_image(file_location):
    encoded_image = Image.open(file_location)

    red_channel = encoded_image.split()[0]


    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]

    decoded_image = Image.new("L", encoded_image.size)

    pixels = decoded_image.load()

    for x in range(x_size):
        for y in range(y_size):
            red = red_channel.getpixel((x,y))
            binary = (bin(red))
            
            if binary[len(binary)-1] == "1":
                pixels[x, y] = (255)
            else:
                pixels[x, y] = (0)
    
    decoded_image.save("decoded_image.png")
