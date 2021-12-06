from drawbot_skia.drawbot import *
import random
import datetime
import math
import numpy as np
from PIL import Image

output_path = '../output/'
input_path = '../input/'
output_scale = 20
padding = 0 
ts = str(datetime.datetime.now().timestamp())

bayer = (
    (0, 8, 2, 10),
    (12, 4, 14, 6),
    (3, 11, 1, 9),
    (15, 7, 13, 5)
)

n = len(bayer)
print("Bayer Matrix:  " + str(n) + "x" + str(n))


def draw_image(input, target_size):
    thresholds = []
    input_image = Image.open(input_path + input)
    image = input_image.rotate(180)
    image = image.transpose(Image.FLIP_LEFT_RIGHT)
    image.thumbnail((target_size, target_size), Image.ANTIALIAS)
    image.rotate(180)

    size(image.width * output_scale + padding * 2,
         image.height * output_scale + padding * 2)
    fill(.0, .0, .0, 1)
    rect(0, 0, image.width * output_scale + padding * 2,
         image.height * output_scale + padding * 2)

    print("Image size:  " + str(image.width) + "x" + str(image.height))

    # Let's make a threshold matrix the size of the input matrix
    # We do that by repeating the Bayer matrix
    print("Computing threshold matrix...")

    bi = [0, 0]

    for i in range(image.height):
        row = []
        for j in range(image.width):
            bi[0] = j % n
            bi[1] = i % n
            # Rescale to -.5, .5 while we're here
            row.append(bayer[bi[1]][bi[0]] * (1 / (n*n)))
        thresholds.append(row)

    print(np.matrix(thresholds))
    print("Matrix size: " +
          str(len(thresholds[0])) + "x" + str(len(thresholds)))
    print("Drawing...")
    for i, pixel in enumerate(image.getdata(), 0):
        x = i % image.width
        y = math.floor(i / image.width)
        #print(pixel[:3])
        average = sum(pixel[:3]) / (255 * 3) - .01
        if (average < thresholds[y][x]):
            # fill(.105, .1, 1, 1)
            fill(0, 0, 0, 1)
        else:
            fill(1, 1, 1, 1)

        # oval(x * output_scale + padding, y * output_scale + padding, output_scale, output_scale)
        rect(x * output_scale + padding, y * output_scale + padding, output_scale, output_scale)


# draw_image("dom-hill-nimElTcTNyY-unsplash.jpg", 50)
draw_image("type3.png", 260)
saveImage(output_path + ts + ".png")
