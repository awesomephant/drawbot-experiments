from drawbot_skia.drawbot import *
import numpy as np
from PIL import Image
import datetime
import math

img = Image.open('../input/acre-logo.png').convert('RGB').transpose(Image.FLIP_LEFT_RIGHT).rotate(180)
bitmap = np.array(img)
rows,cols,channels = bitmap.shape
pixels = bitmap.reshape((rows*cols, 3))
print(bitmap.shape)
print(pixels.shape)

output_path = "../output/acre/"
ts = str(datetime.datetime.now().timestamp())

canvas_width = 10000
# canvas_height = canvas_width * math.sqrt(2)
canvas_height = canvas_width / 10 
margin = 25
cols = 100
rows = 100

def fill_hatching(x,y,width,height):
    lineCount = 1
    stroke(1,1,1,1)
    # sw = (math.sin(y / 5) + .5)  * 5
    strokeWidth(5)
    for i in range(lineCount):
        y0 = y + (height / lineCount * i)
        y1 = y + (height / lineCount * (i + 1))
        x0 = x
        x1 = x + width
        line((x0, y0), (x1, y1))

def draw_grid(x0, y0, width, height, rows, cols):
    fill(0,0,0,0)
    stroke(.2,.2,.2,1)
    strokeWidth(1)
    rect(x0, y0, width, height)
    for i in range(cols):
        x = x0 + (i % cols) * (width / cols)
        line((x, y0), (x, height))
    for i in range(rows):
        y = y0 + (i % rows) * (height / rows)
        line((x0, y), (width, y))

def draw_logo(pixels, x0, y0, width, height, rows, cols):
    fill(1,1,1,1)
    cell_width = width / cols
    cell_height = height / rows
    for i in range(len(pixels)):
        x = (i % rows) * (width / cols) + x0
        y = y0 + (math.floor(i / rows) * (height / cols))
        if(sum(pixels[i]) < 700):
            rect(x,y,cell_width, cell_height)
            # fill_hatching(x,y,cell_width, cell_height)

def draw():
    fill(0, 0, 0, 1)
    rect(0, 0, canvas_width, canvas_height)
    draw_logo(pixels, margin, margin, canvas_width - margin * 2, canvas_height - margin * 2, rows, cols)
    draw_grid(margin, margin, canvas_width - margin * 2, canvas_height - margin * 2, rows, cols)


size(canvas_width, canvas_height)

draw()
saveImage(output_path + "test" + ".png")
# saveImage(output_path + ts + ".png")
