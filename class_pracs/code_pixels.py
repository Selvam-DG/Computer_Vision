import numpy as  np
import cv2

## Read the image
img = cv2.imread("Car.jpg",1)
print(img.shape)

px= img[100, 100]
print(px)

# access only blue pixel - OpenCV read images as BRG format
blue = img[100,100,0] # 1st channel in color image is Blue
print("Blue pixel value = ", blue)

# access red pixel
red = img.item(10,10,2) # 3rd channel is RED
print(red)

# modify pixel value
img.itemset((10,10,2), 255)
print(img.item(10,10,2))

# separate channels
# b,g,r = cv2.split(img) 

# img[:,:,0] = 0
# img[:,:,1] = 0
# img[:,:,2] = 0

#selecting particular mark

# tick = img[200:230, 120:150]
# img[120:150,100:130] = tick


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()