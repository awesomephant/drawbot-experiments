from drawbot_skia.drawbot import *
import random
import datetime
import math
from rounded_rect import rounded_rect

ts = str(datetime.datetime.now().timestamp())


class Space:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h


def coin(p=.5):
    v = random.random()
    if v < p:
        return True
    return False


# Configuration
output_path = '../output/'
input_path = '../input/'

padding = 2
margin = 10
w = 1080 + (margin * 2)
h = 1350 + (margin * 2)
iterations = 7

spaces = [
    Space(margin, margin, w - margin * 2, h - margin * 2)
]
final_spaces = []

size(w, h)
split_proportions = [1/2, 1/3, 1/4]
colours = [
    (1, 0, 0, 1),
    (0, 1, 0, 1),
    (0, 0, 1, 1)
]


for i in range(iterations):
    new_spaces = []
    for s in spaces:
        toss = True
        if i > 2:
            toss = coin(.75)

        if toss:
            # Split
            proportion = random.choice(split_proportions)
            if s.w > s.h:
                new_spaces.append(Space(s.x, s.y, s.w * proportion, s.h))
                new_spaces.append(
                    Space(s.x + s.w * proportion, s.y, s.w * (1 - proportion), s.h))
            else:
                new_spaces.append(Space(s.x, s.y, s.w, s.h * proportion))
                new_spaces.append(
                    Space(s.x, s.y + s.h * proportion, s.w, s.h * (1 - proportion)))
        else:
            # Fill
            final_spaces.append(s)
    spaces = new_spaces

final_spaces = final_spaces + spaces

fill(0, 0, 0, 1)
rect(0, 0, w, h)

for s in final_spaces:
    fill(*random.choice(colours))
    rounded_rect(s.x, s.y, s.w - padding, s.h - padding, 10, .2)


saveImage(output_path + ts + ".png")
