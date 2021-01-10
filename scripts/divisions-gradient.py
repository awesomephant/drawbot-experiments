from drawbot_skia.drawbot import *
import random
import datetime
import math
from rounded_rect import rounded_rect
from coin import coin

ts = str(datetime.datetime.now().timestamp())


class Space:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h


# Configuration
output_path = '../output/'
input_path = '../input/'

padding = 1
margin = 10
w = 1080 + (margin * 2)
h = 1350 + (margin * 2)
iterations = 5

split_proportions = [1/2, 1/3, 1/4, 3/5]

def draw():
    spaces = [Space(margin, margin, w - margin * 2, h - margin * 2)]
    final_spaces = []
    newPage(w, h)
    frameDuration(.2)
    for i in range(iterations):
        new_spaces = []
        for s in spaces:
            toss = True
            if i > 2:
                toss = coin(.7)

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

    primary = (0.95, 0.41, .05, 1)
    fill(*primary)
    rect(0, 0, w, h)
    colors = [primary, (.93, .93, .93, 1)]
    for s in final_spaces:
        random.shuffle(colors)
        if s.w > s.h:
            start = (s.x, s.y)
            end = (s.x + s.w, s.y)
        else:
            start = (s.x, s.y)
            end = (s.x, s.y + s.h)

        linearGradient(start, end, colors, [.1, .9])
        radius = (s.w * s.h) / 1500
        rounded_rect(s.x, s.y, s.w - padding, s.h - padding, radius, .3)


draw()
saveImage(output_path + ts + ".png")
