import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((640,480,3),np.uint8)
# O Symbol
cv.ellipse(img, (210,120), (50,50),20,-255,35,(0,0,255),20)
# C symbol
cv.ellipse(img, (150,250), (50,50),20,-15,265,(0,255,0),20)
# Vsymbol
cv.ellipse(img, (290,250), (50,50),20,-90,200,(255,0,0),20)

cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()