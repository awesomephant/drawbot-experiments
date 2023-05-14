from drawbot_skia.drawbot import * 

def draw_grid(x0, y0, width, height, rows, cols):
    rect(x0, y0, width, height)
    for i in range(cols - 1):
        x = x0 + (i + 1 % cols) * (width / cols)
        line((x, y0), (x, height+ y0))
    for i in range(rows - 1):
        y = y0 + (i + 1 % rows) * (height / rows)
        line((x0, y), (width + x0, y))