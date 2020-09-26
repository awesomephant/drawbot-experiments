from drawbot_skia.drawbot import *
import random
import datetime
import math


def coin():
    v = random.random()
    if v > .5:
        return True
    return False


output_path = '../output/'
input_path = '../input/'
ts = str(datetime.datetime.now().timestamp())

cols = 6
rows = 3

possible_glyphs = list("abcdefgABCDEFG")
print(possible_glyphs)
iterations = 100
scale = 300

size(cols * scale, rows * scale)
fill(0, 0, 0, 1)
rect(0, 0, 1000, 1000)

font("Ornaments", scale)


def fillGrid():
    r = random.random()
    fill(r, r, r, 1)
    for cell in range(cols * rows):
        x = cell % cols
        y = math.floor(cell / cols)
        if coin():
            text(random.choice(possible_glyphs), (x * scale, y * scale))


for i in range(iterations):
    fillGrid()

saveImage(output_path + ts + ".png")
