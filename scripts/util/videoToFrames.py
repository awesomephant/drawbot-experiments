import cv2

vidcap = cv2.VideoCapture("../../input/test.mp4")
success, image = vidcap.read()
count = 0
while success and count < 2000:
    cv2.imwrite("frame%d.png" % count, image)
    success, image = vidcap.read()
    print("Wrote frame ", count)
    count += 1
