import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("Car.jpg",1)


height, width = image.shape[:2]

# res = cv2.resize(img, None, fx=1, fy=1, interpolation= cv2.INTER_CUBIC)

res = cv2.resize( image, (800,800), interpolation= cv2.INTER_CUBIC)


cv2.imshow('image', image)
cv2.waitKey(0)
cv2.imshow('scaled_image', res)
cv2.waitKey(0)
cv2.destroyAllWindows()