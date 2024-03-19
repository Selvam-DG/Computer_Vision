import cv2 as cv
import numpy as np

############ SIMPLE DETECT the pixel value on the click ################

# img = cv.imread('Messi.jpg')
# img = cv.resize(img, (640,480))
# def mousePoints(event, x, y, flags, params):
#     if event == cv.EVENT_LBUTTONDOWN:
#         # print the pixel positions in the image
#         print(x,y)
# cv.imshow('Image', img)
# cv.setMouseCallback('Image', mousePoints)
# cv.waitKey(0)
# cv.destroyAllWindows()

############## Creating a image from the clicks and wrap them from those points ###########

img = cv.imread('Messi.jpg')
img = cv.resize(img, (640,480))
circles = np.zeros((4,2),np.int)
count = 0


# get pixel values from the pic on clicks with mouse
def mousePoints(event, x,y, flag, params):
    global count
    if event == cv.EVENT_LBUTTONDOWN:
        circles[count] = x,y
        count+=1
        print(circles)

while True:
    cv.imshow('Original Image', img)   
    for x in range(0,4):
        cv.circle(img, (circles[x][0], circles[x][1]), 5, (0,255,0), cv.FILLED)
    cv.setMouseCallback('Original Image', mousePoints)

    # image transfomation from the selected pixel values
    if count == 4:
        width, height = 640,480
        pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        pts2 = np.float32([[0,0],[width, 0], [0, height], [width, height]])
        matrix = cv.getPerspectiveTransform(pts1, pts2)
        imgOutput = cv.warpPerspective(img, matrix, (width, height))
        cv.imshow('OutputImage', imgOutput)

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()