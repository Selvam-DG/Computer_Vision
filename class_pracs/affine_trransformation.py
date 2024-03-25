import  numpy as np
import cv2

img = cv2.imread("Car.jpg",0)
rows,cols = img.shape

M = np.float32([[0,0,0], [0,0,0]])

dst = cv2.warpAffine(img, M, (rows, cols))

cv2.imshow('image', img)
cv2.waitKey(0)

# Rotation

M = cv2.getRotationMatrix2D((cols/2, rows/2),45,1)

rot = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('rotateimage', rot)
cv2.waitKey(0)

cv2.destroyAllWindows()