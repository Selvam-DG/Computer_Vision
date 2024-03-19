import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

############### STACKING IMAGES #############################
# img = cv.imread("Messi.jpg")
# img =  cv.resize(img, (640,480))
# img1 = cv.imread("Ronaldo.jpg")
# print(img1.shape)
# img1 =  cv.resize(img1, (640,480))

# grayImg = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# grayImg1 = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)

# horStack = np.hstack((img, img1))
# horStack = cv.resize(horStack, (640,480))
# verStack = np.vstack((img,img1))
# verStack = cv.resize(verStack, (640,480))
# # cv.imshow(img, grayImg)
# cv.imshow("hstack", horStack)
# cv.imshow("Vertical stack", verStack)
# cv.waitKey(0)
# cv.destroyAllWindows()

def stackImages(imgArray, scale, lables=[]):
    sizew = imgArray[0][0].shape[1]
    sizeh = imgArray[0][0].shape[0]
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowAvailabe = isinstance(imgArray[0], list) # checking whether imagArray 1st element is list or not
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowAvailabe:
        for i in range(0, rows):
            for j in range(0,cols):
                imgArray[i][j] = cv.resize(imgArray[i][j], (sizew,sizeh), None, scale, scale)
                if len(imgArray[i][j].shape)==2:
                       imgArray[i][j] = cv.cvtColor(imgArray[i][j], cv.COLOR_GRAY2BGR, None)
        imgBlank = np.zeros((height, width,3),np.uint8)
        horstack = [imgBlank]*rows
        horstack_con = [imgBlank]*rows
        for i in range(0,rows):
            horstack[i] = np.hstack(imgArray[i])
            horstack_con = np.concatenate(imgArray[i])
        verstack = np.vstack(horstack)
        verstack_con = np.concatenate(horstack)
    else:
        for i in range(0, rows):
            imgArray[i] = cv.resize(imgArray[i], (sizew, sizeh), None, scale, scale)
            if len(imgArray[i].shape)==2:
                       imgArray[i] = cv.cvtColor(imgArray[i], cv.COLOR_GRAY2BGR)
        horstack = np.hstack(imgArray)
        horstack_con = np.concatenate(imgArray)
        verstack = horstack
    if len(lables)!=0:  
         eachImgWidth = int(verstack.shape[1]/cols)
         eachImgHeight = int(verstack.shape[0]/cols)
        #  print(eachImgHeight)

         for d in range(0, rows):
            for c in range (0,cols):
                cv.rectangle(verstack,(c*eachImgWidth,eachImgHeight*d),(c*eachImgWidth+len(lables[d][c])*13+27,30+eachImgHeight*d),(255,255,255),cv.FILLED)
                cv.putText(verstack,lables[d][c],(eachImgWidth*c+10,eachImgHeight*d+20),cv.FONT_HERSHEY_COMPLEX,0.7,(255,0,255),2)
    return verstack
        
            
        



cap = cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    rec,frame = cap.read()
    kernel = np.ones((5,5),np.uint8)
    grayFrame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY, None)
    gausBlur = cv.GaussianBlur(grayFrame,(5,5),0, None)
    cannyEdge = cv.Canny(gausBlur,50,150)
    dilateFrame = cv.dilate(cannyEdge, kernel=kernel,iterations=2)
    erodeFrame = cv.erode(dilateFrame, kernel=kernel, iterations=2)
    stackedImages = stackImages(([frame, grayFrame, gausBlur],[cannyEdge, dilateFrame, erodeFrame]), 0.5)
    k = cv.waitKey(1) & 0xFF
    

    cv.imshow('Stacked Image', stackedImages)
    if k== ord('q'):
        break

cap.release()
cv.destroyAllWindows()