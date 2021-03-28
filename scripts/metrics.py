from drawbot_skia.drawbot import *

output_path = '../output/'
input_path = '../input/'
# set font to something i've synced with adobe fonts
font('Cooper Black Std', 100)

size(1000, 1000)
fill(0, 0, 0, 1)
text("Hello World", (10, 10))

saveImage(output_path + "test" + ".png")