import  numpy as np
import cv2
from matplotlib import pyplot as plt
image = cv2.imread("Car.jpg",1)

# openCV provides a function , cv2.filter2d to convolute a kernel with an image
# average filter
kernel = np.ones((5,5), np.float32)/25
distort = cv2.filter2D(image, 0, kernel)

plt.subplot(121), plt.imshow(image), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(distort), plt.title('Average_convolution')
plt.xticks([]), plt.yticks([])
plt.show()

#Average blur
blur = cv2.blur(image, (5,5))

plt.subplot(121), plt.imshow(image), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(blur), plt.title('Average_Blur')
plt.xticks([]), plt.yticks([])
plt.show()

#Gaussiann filter
gaussina_blur = cv2.GaussianBlur(image, (5,5), 0)

plt.subplot(121), plt.imshow(image), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(gaussina_blur), plt.title('Gaussian_blur')
plt.xticks([]), plt.yticks([])
plt.show()


# median filter
median_blur = cv2.medianBlur(image, 5)

plt.subplot(121), plt.imshow(image), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(median_blur), plt.title('median_blur')
plt.xticks([]), plt.yticks([])
plt.show()
