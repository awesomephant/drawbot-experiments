from drawbot_skia.drawbot import *
import random
import datetime
import math
from rounded_rect import rounded_rect

size(1000, 1000)
linearGradient(
    (100, 100),                         # startPoint
    (800, 800),                         # endPoint
    [(1, 0, 0), (0, 0, 1), (0, 1, 0)],  # colors
    [0, .2, 1]                          # locations
)
rect(100,100,400,600)
output_path = '../output/'
saveImage(output_path + "test.png")