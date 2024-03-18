import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread("Messi.jpg")
# resize the image to 640x480
resizeImage = cv.resize(image, (640,480),None)

# grayscale image
grayImg = cv.cvtColor(resizeImage, cv.COLOR_BGR2GRAY)

# gaussian blur
GausImg = cv.GaussianBlur(grayImg, (5,5),0.1)

# cannyEdge detection
cannyImage = cv.Canny(GausImg,100,200)

# dilate the image
dilateImg = cv.dilate(cannyImage, kernel=np.ones((5,5),np.uint8),iterations=10)

# Erode the image
erodeImg = cv.erode(dilateImg, kernel= np.ones((5,5),np.uint8), iterations=5)

imgName = ['Original Image','ResizedImage','GaussianBlurrredImage', 'Canny Edge Detection',
            'Dilated Image','Eroded Image']
img = [image, resizeImage ,GausImg, cannyImage, dilateImg, erodeImg]
i=0
for image in img:
    cv.imshow(imgName[i], image)
    k = cv.waitKey()
    if k == 27: # press any key to move to next pic
        cv.destroyAllWindows()
        continue
    elif k == ord("q"): # press q to exit
        cv.destroyAllWindows()
        break
    i+=1

# display the output
# cv.imshow("Image",image)
# cv.imshow("Gaussian Blured Image", GausImg)
# cv.imshow("Canny Edge Detection", cannyImage)
# cv.imshow("Dilated Image", dialteImg)
# cv.imshow("Eroded Image", erodeImg)
# clear the window
# cv.waitKey(0)
cv.destroyAllWindows()