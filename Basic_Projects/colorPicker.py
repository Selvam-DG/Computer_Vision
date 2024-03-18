import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
cap.set(3,640) # set the width of the frame to 640
cap.set(4, 480) #set the height of the frame to 480

def nothing(x):
    pass

def stackImages(scale, imagArray):
    row = len(imagArray)  # first value in th shape of image
    col = len(imagArray[0]) # Number of columns in the first row
    rowsAvailable = isinstance(imagArray[0], list)
    width = imagArray[0][0].shape[1]
    height = imagArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0,row):
            for y in range(0, col):
                if imagArray[x][y].shape[:2] == imagArray[0][0].shape[:2]:
                    imagArray[x][y] = cv.resize(imagArray[x][y], (0,0), None, scale, scale)
                else:
                    imagArray[x][y] = cv.resize(imagArray[x][y], (imagArray[0][0].shape[1],imagArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imagArray[x][y].shape) ==2:
                    imagArray[x][y] = cv.cvtColor(imagArray[x][y],cv.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * row
        nor_col = [imageBlank] * row

        for x in range(0, row):
            hor[x]  = np.hstack(imagArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, row):
            if imagArray[x].shape[:2] == imagArray[0].shape[:2]:
                imagArray[x] = cv.resize(imagArray[x], (0,0), None, scale, scale)
            else:
                imagArray[x] = cv.resize(imagArray[x], (imagArray[0].shape[1],imagArray[0].shape[0]),
                                                None, scale, scale)
            if len(imagArray[x].shape)==2:
                imagArray[x] = cv.cvtColor( imagArray[x], cv.COLOR_GRAY2BGR)
        hor = np.hstack(imagArray)
        ver = hor

    return ver


# img = cv.imread('Messi.jpg')
# print(len(img[745]))
# stackImages(0.8,img)

### create colorsaturation window for adjust the HSV level '
cv.namedWindow('TrackBars')
cv.resizeWindow('TrackBars', 300,512)
cv.createTrackbar('Hue Min', 'TrackBars', 0,179, nothing)
cv.createTrackbar('Hue Max', 'TrackBars', 179,179, nothing)
cv.createTrackbar('Sat Min', 'TrackBars', 0,255, nothing)
cv.createTrackbar('Sat Max', 'TrackBars', 255,255, nothing)
cv.createTrackbar('Val Min', 'TrackBars', 0, 255, nothing)
cv.createTrackbar('Val Max', 'TrackBars', 255, 255, nothing)

while True:
    ret, frame = cap.read()
    # frame = cv.imread('Messi.jpg')
    frame = cv.resize(frame, (300,512), None)
    

    imgHSV =  cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    h_min = cv.getTrackbarPos('Hue Min',"TrackBars")
    h_max = cv.getTrackbarPos('Hue Max', 'TrackBars')
    s_min = cv.getTrackbarPos('Sat Min', 'TrackBars')
    s_max = cv.getTrackbarPos('Sat Max', 'TrackBars')
    v_min = cv.getTrackbarPos('Val Min', 'TrackBars')
    v_max = cv.getTrackbarPos('Val Max', 'TrackBars')

    print(f'hue range = ({h_min}, {h_max}), Satn range = ({s_min},{s_max}), val range= ({v_min}, {v_max})')
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv.inRange(imgHSV, lower, upper)

    imgResult = cv.bitwise_and(frame, frame, mask=mask)

    # cv.imshow('Original', frame)
    # cv.imshow('HSV', imgHSV)
    # cv.imshow('Mask', mask)
    # cv.imshow('Result', imgResult)

    imgStack = stackImages(0.6, ([frame, imgHSV],[mask, imgResult]))
    cv.imshow('Stacked images', imgStack)

    k = cv.waitKey(1)
    if k ==27:
        break
cap.release()
cv.destroyAllWindows()