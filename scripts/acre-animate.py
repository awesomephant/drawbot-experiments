from drawbot_skia.drawbot import *
import numpy as np
from PIL import Image
import datetime
import math
import json


img = Image.open('../input/acre-logo.png').convert('RGB').transpose(Image.FLIP_LEFT_RIGHT).rotate(180)
bitmap = np.array(img)
rows,cols,channels = bitmap.shape
pixels = bitmap.reshape((rows*cols, 3))

output_path = "../output/acre/"
ts = str(datetime.datetime.now().timestamp())

canvas_width = 3000
# canvas_height = canvas_width * math.sqrt(2)
canvas_height = canvas_width * .66
margin = 0
cols = 100
rows = 100
lines = []

class Line():
    def __init__(self, p0, p1):
        self.p0 = p0
        self.p1 = p1

def fill_hatching(x,y,width,height, offset=1, skip_bottom=False, skip_top=False):
    lineCount = 3
    sb = 0
    st = 0
    if (skip_bottom):
        sb = 1

    if (skip_top):
        st = -1
    
    strokeWidth(.003 * y)
    
    for i in range(sb, lineCount + st):
        y0 = y + (height / lineCount * i)
        y1 = y + (height / lineCount * (i + offset))
        x0 = x
        x1 = x + width
        line((x0, y0), (x1, y1))
        lines.append([[x0,y0], [x1, y1]])

def draw_grid(x0, y0, width, height, rows, cols):
    strokeWidth(1)
    rect(x0, y0, width, height)
    for i in range(cols):
        x = x0 + (i % cols) * (width / cols)
        line((x, y0), (x, height))
    for i in range(rows):
        y = y0 + (i % rows) * (height / rows)
        line((x0, y), (width, y))

def draw_logo(pixels, x0, y0, width, height, rows, cols):
    cell_width = width / cols
    cell_height = height / rows
    for i in range(len(pixels)):
        x = (i % rows) * (width / cols) + x0
        y = y0 + (math.floor(i / rows) * (height / cols))
        if(sum(pixels[i]) < 700):
            skip_bottom = False
            skip_top = False
            if(pixels[i][0] > 100):
                skip_bottom = True
            if(pixels[i][1] > 100):
                skip_top = True
            fill_hatching(x,y,cell_width, cell_height, 1, skip_bottom=skip_bottom, skip_top=skip_top)
            # rect(x,y,cell_width, cell_height)

def draw():
    # rect(0, 0, canvas_width, canvas_height)
    # stroke(.1,.1,.1,.9)
    # draw_grid(margin, margin, canvas_width - margin * 2, canvas_height - margin * 2, rows, cols)
    # fill(1, 1, 1, 1)
    stroke(0,0,0,1)
    draw_logo(pixels, margin, margin, canvas_width - margin * 2, canvas_height - margin * 2, rows, cols)


size(canvas_width, canvas_height)

draw()
# saveImage(output_path + "acre-hatched" + ".svg") 

# with open(output_path + 'acre.json', 'w', encoding='utf-8') as f:
#     json.dump(lines, f, indent=2)
# saveImage(output_path + "acre-hatched" + ".png") 

saveImage(output_path + "test" + ".svg")

# Size: LineCount / StrokeWidth
# Small: 1 / 5