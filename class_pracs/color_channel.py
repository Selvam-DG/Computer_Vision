import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("Car.jpg",1)
iamge = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# blue channel
r= image.copy()
b[:,:,1] = 0
b[:,:,2] = 0

# green channel
g = image.copy()
g[:,:,0] = 0
g[:,:,2] = 0

#red Channel
r = image.copy()
r[:,:,0] = 0
r[:,:,1] = 0


plt.subplot(2,2,1), plt.imshow(image), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2), plt.imshow(r), plt.title('Blue-Channel') # matplotlib read images as RGB whereas Opencv read images as BRG
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3), plt.imshow(g), plt.title('Green-Channel')
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4), plt.imshow(b), plt.title('Red-Channel')
plt.xticks([]), plt.yticks([])
plt.show()

# cv2.imshow('B-RGB',b)
# cv2.imshow('G-RGB', g)
# cv2.imshow('R-RGB', r)
cv2.waitKey(0)
cv2.destroyAllWindows()