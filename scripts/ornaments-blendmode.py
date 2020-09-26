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

cols = 3
rows = 3

possible_glyphs = list("abcdefghABCDEFGH")
print(possible_glyphs)
iterations = 7
scale = 600

size(cols * scale, rows * scale)
fill(.9,.9,.9, 1)
rect(0, 0, 10000, 10000)

font("Ornaments", scale)
blendMode('multiply')

def fillGrid():
    fill(random.random(), random.random(), random.random(), 1)
    for cell in range(cols * rows):
        x = cell % cols
        y = math.floor(cell / cols)
        if coin():
            text(random.choice(possible_glyphs), (x * scale, y * scale))


for i in range(iterations):
    fillGrid()

saveImage(output_path + ts + ".png")
