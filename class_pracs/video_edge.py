import numpy as np
import cv2

# capture livestream video

cap = cv2.VideoCapture(0)

while(True):
    rec, frame = cap.read()
    
    # covert to HSV for simpler calculations
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # calculation of SobleX
    sobelX = cv2.Sobel(frame, cv2.CV_64F, 1,0, ksize=5)
    
    #calculation of SobelY
    sobelY = cv2.Sobel(frame, cv2.CV_64F, 0,1, ksize=5)
    
    # calculation of Laplacian
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    
    cv2.imshow('sobelX', sobelX)
    cv2.imshow('SobelY', sobelY)
    cv2.imshow('Laplacian', laplacian)
    
    k = cv2.waitKey(1) & 0xFF
    if k==27: # press esc button to exit the loop
        break
    
cv2.destroyAllWindows()

# release the frame
cap.release()
    