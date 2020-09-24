from drawbot_skia.drawbot import *
import random
import datetime
output_path = './output/'


def coin():
    v = random.random()
    if v > .5:
        return True
    return False


ts = str(datetime.datetime.now().timestamp())
iterations = 100
w = 1000
h = 1000
padding = 1
possible_grids = [2, 4, 10, 20, 40]

size(w, h)

fill(0, 0, 0)
rect(0, 0, w, h)

fill(1, 1, 1, 1)

for i in range(iterations):
    columns = random.choice(possible_grids)
    rows = columns
    column_delta = w / columns
    row_delta = h / rows
    fill(random.random(), random.random(), random.random(), 1)
    if coin():
        fill(0, 0, 0, 1)

    for c in range(columns):
        for r in range(rows):
            if coin():
                rand = random.random()
                if rand > .2:
                    rect(column_delta * c, row_delta * r,
                         column_delta - padding, row_delta - padding)
            else:
                rand = random.random()
                if rand > .2:
                    oval(column_delta * c, row_delta * r,
                         column_delta - padding, row_delta - padding)

saveImage(output_path + ts + ".png")
