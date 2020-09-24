from drawbot_skia.drawbot import *
import random
import datetime
import math
from PIL import Image


def coin():
    v = random.random()
    if v > .5:
        return True
    return False


output_path = '../output/'
input_path = '../input/'
ts = str(datetime.datetime.now().timestamp())

size(1000, 1000)
fill(0, 0, 0, 1)
rect(0, 0, 1000, 1000)


def draw_image(input, target_size):
    input_image = Image.open(input_path + input)
    image = input_image.rotate(180)
    image.thumbnail((target_size, target_size), Image.ANTIALIAS)
    image.rotate(180)

    imageWidth = image.width
    imageHeight = image.height

    scaleY = 1000 / imageHeight
    scaleX = scaleY

    if coin():
        fill(random.random(), random.random(), random.random(), .9)
        fill(1,1,1,1)
    else:
        fill(0,0,0,1)

    mode = "c"
    if coin():
        mode = "c"

    for i, pixel in enumerate(image.getdata(), 1):
        x = i % imageWidth
        y = math.floor(i / imageWidth)
        if type(pixel) is tuple:
            average = (sum(pixel) / 3) / 255
        else:
            average = pixel / 255

        if mode == "v":
            rect(x * scaleX, y * scaleY, scaleX, scaleY * average)
        if mode == "c":
            oval(x * scaleX, y * scaleY, scaleX * average, scaleY * average)
        else:
            rect(x * scaleX, y * scaleY, scaleX * average, scaleY)


draw_image("C_Venera09_Oct26e.jpg", 10)
draw_image("C_Venera09_Oct26e.jpg", 1000)
draw_image("C_Venera09_Oct26e.jpg", 10)
draw_image("Capture.PNG", 20)
draw_image("V_Venera9c.jpg", 5)
draw_image("Capture.PNG", 20)
saveImage(output_path + ts + ".png")
