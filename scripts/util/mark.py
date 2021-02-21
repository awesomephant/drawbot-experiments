from drawbot_skia.drawbot import rect
def mark(p, r=8, active=True):
    x = p[0]
    y = p[1]
    if active:
        rect(x - r / 2, y - r / 2, r, r)
    return
