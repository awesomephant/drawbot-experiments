from drawbot_skia.drawbot import rect


def draw_grid(x_0, y_0, w, h, interval=10, r=8):
    cols = w // interval
    rows = h // interval

    for i in range(rows):
        for j in range(cols):
            x = x_0 + (w / cols) * j
            y = 1000
            rect(x, y, r, r)
    return
