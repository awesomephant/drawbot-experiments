from contextlib import closing
from drawbot_skia.drawbot import *
import random
import datetime
import math
import time
from PIL import Image

output_path = "../output/"
input_path = "../input/"

w = 2000
h = 1500


def draw_image(input, output, target_size):
    newDrawing()
    size(w, h)
    t_start = time.perf_counter()
    input_image = Image.open(input_path + input)
    image = input_image.rotate(180)
    image.thumbnail((target_size, target_size), Image.ANTIALIAS)

    imageWidth = image.width
    imageHeight = image.height

    scaleY = h / imageHeight
    scaleX = scaleY
    padding = 0
    fill(.93, .95, 0.94, 1)
    rect(0, 0, w, h)
    fill(.0, 00, 0.0, 1)

    for i, pixel in enumerate(image.getdata(), 0):
        x = i % imageWidth
        y = math.floor(i / imageWidth)

        if type(pixel) is tuple:
            value = (sum(pixel) / 4) / 255
        else:
            value = pixel / 255
        rect(x * scaleX, y * scaleY, scaleX * 1.1, 1.1 * scaleY * (value + .4))

    saveImage(output_path + output)

    input_image.close()
    image.close()

    t_end = time.perf_counter()
    print(
        "Wrote "
        + output_path
        + output
        + " ("
        + str(t_end - t_start)
        + "s)"
        + " scale: "
        + str(scale)
    )


scale = 100
offset = 0
maxFrame = 1000
d = 1
for i in range(offset, maxFrame):
    draw_image(
        "frames/frame" + str(i) + ".png", "video/" + str(i - offset) + ".png", scale
    )
