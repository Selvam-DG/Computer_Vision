import numpy as np
import cv2

# 0 is default camera/webcam
# 1 is usb camera

cap = cv2.VideoCapture(0)
count = 0
while(True):
    # capture frame by frame by frame
    ret, frame = cap.read()
    #Our operation on the frame come here
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # print(frame.shape, type(ret))
    
    #Display the resulting frame
    # print(gray)
    
    # # accessing R,G,B channels
    # frame1 = frame.copy()
    # frame1[:,:,0] = 0
    # frame1[:,:,1] = 0
    
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('Image0' + str(count) + 'png', gray)
        print(count)
        count+=1
        

# when everything done, release the capture
cap.release()
cv2.destroyAllWindows()

# Assignment  run this same experiments with a video file: avi, mp4