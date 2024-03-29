from contextlib import closing
from drawbot_skia.drawbot import *
import random
import datetime
import math
import time
from PIL import Image

output_path = "../output/"
input_path = "../input/"

glyphs = list("cdfghj ABCDEEFIKLYXZ")
random.shuffle(glyphs)
w = 2000
h = 1500


def value_to_glyph(v):
    interval = 1 / len(glyphs)
    return glyphs[math.floor(v / interval) - 1]


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
    font("Ornaments", scaleX - padding + 2)
    fill(0.95, 0.95, 0.95, 1)
    rect(0, 0, w, h)
    fill(0, 0.0, 0.0, 1)

    for i, pixel in enumerate(image.getdata(), 0):
        x = i % imageWidth
        y = math.floor(i / imageWidth)

        if type(pixel) is tuple:
            value = (sum(pixel) / 4) / 255
        else:
            value = pixel / 255

        text(value_to_glyph(value), (x * scaleX, y * scaleY))

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


scale = 10
offset = 827
maxFrame = 1000
d = 1
for i in range(offset, maxFrame):
    # if (i % 72 == 0):
    #     scale = random.randrange(30, 300)
    #     random.shuffle(glyphs)
    if i > 300 + offset:
        d = -1
    scale += d

    draw_image("frames/frame" + str(i) + ".png", "video/" + str(i - offset) + ".png", scale)
