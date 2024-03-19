import cv2 as cv
import numpy as np

# img = cv.imread("Messi.jpg")
img = np.zeros((640,480,3), np.uint8)

blue = img.copy()
blue[:] = 255,0,0
# draw a diagonal lines  in the picture
cv.line(blue,  (0,0),(480,blue.shape[0]),(0,0,255),5)
cv.line(blue, (blue.shape[1],0), (0, blue.shape[0]), (255,255,255), 5)

# draw a cirlces in the centre of the picture
cv.circle(blue, (int(blue.shape[1]/2),int(blue.shape[0]/2)),60, (0,255,0),thickness=-1)

# draw a rectagle on the top the circle
cv.rectangle(blue, (100,200),(400,450),(0,255,255),3)

cv.putText(blue, "Drawn Shapes with OPENCV",(20,30),cv.FONT_HERSHEY_COMPLEX,1, (0,0,0),3)
cv.imshow("Blue", blue)
cv.waitKey(0)
cv.destroyAllWindows()