from drawbot_skia.drawbot import *
import datetime
import math
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

class Line():
    def __init__(self, p0, p1):
        self.p0 = p0
        self.p1 = p1

def draw_pie(x,y,r,angle,rotate):
    if angle == 1:
        oval(x - r, y-r, r * 2, r * 2)
        return
    
    startAngle = 90 + rotate * 360
    endAngle = startAngle + (angle * 360) + rotate * 360

    path = BezierPath()
    path.moveTo((x, y))
    path.lineTo((x,y-r))
    path.arc((x,y), r, startAngle, endAngle, False)
    path.lineTo((x,y))
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
    fill(.6,.6,.6, 1)
    # fill(*hex_to_rgb(forest["dark5"]), 1)
    # fill(*hex_to_rgb(violet["dark5"]), 1)
    rect(0, 0, canvas_width, canvas_height)
    padding = 4
    
    for i in range(cols * rows):
        x = i % cols    
        y = math.floor(i / cols)
        x_scaled =  (x/cols) * canvas_width + canvas_width / cols / 2
        y_scaled = (y/rows) * canvas_height + canvas_height / rows / 2

        r = canvas_width / cols * .5 - padding

        # fill(*hex_to_rgb(red["dark5"]), .2 + math.asin(x / cols))
        fill(*hex_to_rgb(plum["light2"]), 1)
        a = math.sin(x / cols)
        r = (canvas_width / cols * .5 - padding)
        r = (canvas_width / cols * 1 - padding) * math.sin(y / rows / 2)
        # draw_pie(x_scaled,y_scaled,r, 1, 0)


        fill(*hex_to_rgb(forest["dark4"]), 1)
        a = math.cos(x / cols * 1) - .2
        r = (canvas_width / cols * .5 - padding)
        # draw_pie(x_scaled,y_scaled,r, a, 0)

        fill(*hex_to_rgb(forest["base"]), 1)
        a = random.uniform(.1,.3)
        # draw_pie(x_scaled,y_scaled,r, a, 0)
    
    fill(1, 1, 1, 0)
    stroke(.35,.35,.35,1)
    stroke(.0,.0,.0,.5)
    # stroke(*hex_to_rgb(forest["dark1"]), 1)
    strokeWidth(1)
    draw_grid(margin, margin, canvas_width - margin * 2, canvas_height - margin * 2, rows, cols)

size(canvas_width, canvas_height)
draw()
saveImage(output_path + "swr-test-7" + ".png")