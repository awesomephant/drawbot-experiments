from drawbot_skia.drawbot import *
import datetime
import math
from opensimplex import noise2
import random

def hex_to_rgb(hex):
    hex = hex.replace("#", "")
    t = tuple(int(hex[i:i+2],16) for i in (0, 2, 4))
    return tuple(n / 255 for n in t)

violet = {
    "light5": '#f3eefa',
    "light4": '#e5dbf5',
    "light3": '#d4c5ee',
    "light2": '#bba4e5',
    "light1": '#9670db',
    "base": '#8257D1',
    "dark1": '#7f4cdf',
    "dark2": '#6830cf',
    "dark3": '#441993',
    "dark4": '#301268',
    "dark5": '#1D0B40'
}

blue= {
    'light5': '#CCDCFF',
    'light4': '#B1C5F9',
    'light3': '#97AEF2',
    'light2': '#7D97EC',
    'light1': '#6280E5',
    'base': '#4768DF',
    'dark1': '#2F51D2',
    'dark2': '#2A3FAC',
    'dark3': '#263187',
    'dark4': '#1c1c64',
    'dark5': '#0b0b40'
}

teal= {
    'light5': '#E5FBFF',
    'light4': '#B9EDF6',
    'light3': '#8CDEEC',
    'light2': '#5BCFE1',
    'light1': '#26BED6',
    'base': '#07ABC5',
    'dark1': '#0698B0',
    'dark2': '#04859C',
    'dark3': '#037389',
    'dark4': '#016275',
    'dark5': '#005163'
}
forest= {
    'light5': '#EFFBE9',
    'light4': '#CEE9D1',
    'light3': '#ADD6BA',
    'light2': '#8CC4A3',
    'light1': '#6BB28B',
    'base': '#499F73',
    'dark1': '#278D5B',
    'dark2': '#137848',
    'dark3': '#0C643A',
    'dark4': '#06502D',
    'dark5': '#003D20'
}

red = {
    'light5': '#ffcfcc',
    'light4': '#FFB9A8',
    'light3': '#FF9B82',
    'light2': '#FF7957',
    'light1': '#FF4D20',
    'base': '#E92F02',
    'dark1': '#C52A04',
    'dark2': '#A22406',
    'dark3': '#801F09',
    'dark4': '#5F1A0B',
    'dark5': '#3F150D'
}

apple= {
    'light5': '#EFFBEA',
    'light4': '#C5F0B1',
    'light3': '#98E472',
    'light2': '#65D62B',
    'light1': '#5BC128',
    'base': '#53AD26',
    'dark1': '#4A9825',
    'dark2': '#438523',
    'dark3': '#3B7122',
    'dark4': '#335E20',
    'dark5': '#2C4C1F'
}

plum = {
    "light5": '#F1CCFF',
    "light4": '#E9AEFF',
    "light3": '#E08EFF',
    "light2": '#D76CFF',
    "light1": '#CB42FF',
    "base": '#B600FB',
    "dark1": '#9903D4',
    "dark2": '#7C05AE',
    "dark3": '#610889',
    "dark4": '#450A65',
    "dark5": '#400E47'
}

output_path = "../output/swrdata/"
ts = str(datetime.datetime.now().timestamp())

canvas_width = 1600
canvas_height = 1200
margin = 0
cols = math.floor(16 * 1.5)
rows = math.floor(12 * 1.5)
lines = []


def draw_wave(xmin, xmax, ymin, noise_y = 0, scale = .1, amplitude = 100, n_points = 100):
    path = BezierPath()
    w = xmax - xmin
    ys = [noise2(x=n * scale, y=noise_y) * amplitude for n in range(n_points)]

    path.moveTo((xmin, 0))
    path.lineTo((xmin, ys[0]))
    for i, y in enumerate(ys):
        path.lineTo((xmin + (w / n_points) * i , ymin + y))

    path.lineTo((xmax, 0))
    drawPath(path)
        

def draw_grid(x0, y0, width, height, rows, cols):
    rect(x0, y0, width, height)
    for i in range(cols):
        x = x0 + (i % cols) * (width / cols)
        line((x, y0), (x, height))
    for i in range(rows):
        y = y0 + (i % rows) * (height / rows)
        line((x0, y), (width, y))


def draw():
    fill(.99,.99,.99, 1)
    # fill(.01,.01,.01, 1)
    rect(0, 0, canvas_width, canvas_height)

    strokeWidth(0)
    stroke(0, 0,0,0)
    for i in range(0,5):
        if random.uniform(0,1) > .5:
            fill(*hex_to_rgb(forest[list(violet.keys())[i]]), 1)
        else:
            fill(*hex_to_rgb(apple[list(violet.keys())[i]]), 1)

        draw_wave(0,canvas_width + 5,canvas_height - 100 - random.uniform(80,150) * (i - 0),
                  scale=random.uniform(.01,.025),amplitude=random.uniform(50,150), n_points=300, noise_y=random.uniform(1,100))
    
    fill(.0,.0,.0,.0)
    stroke(.0,.0,.0,.125)
    strokeWidth(1)
    draw_grid(margin, margin, canvas_width - margin * 2, canvas_height - margin * 2, rows, cols)



size(canvas_width, canvas_height)
draw()
saveImage(output_path + "swr-test-10" + ".png")