import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread("tests/notes.jpg")
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread("resources/quarter_up.jpg", 0)
w, h = template.shape[::-1]


res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.25
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)

cv2.imwrite('tests/output/notes.jpg', img_rgb)
