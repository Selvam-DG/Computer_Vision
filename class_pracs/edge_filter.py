import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('Car.jpg',0)

# Laplacian filter
laplacian = cv2.Laplacian(image, cv2.CV_64F)

#Sobel filter
sobelx = cv2.Sobel(image, cv2.CV_64F, 1,0, ksize=5)
sobely = cv2.Sobel(image, cv2.CV_64F, 0,1, ksize = 5)


plt.subplot(2,2,1), plt.imshow(image, cmap = 'gray'), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2), plt.imshow(laplacian, cmap='gray'), plt.title('Laplacian')
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3), plt.imshow(sobelx, cmap='gray'), plt.title('SobelX')
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4), plt.imshow(sobely, cmap= 'gray'), plt.title('SobleY')
plt.xticks([]), plt.yticks([])

plt.show()