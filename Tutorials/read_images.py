import cv2
import numpy as np


# #Read image
# image = cv2.imread('D:/Data_Science/CV/OpenCV_Projects\Photos/cat_large.jpeg')

# #Display the image using cv2.imshow()
# cv2.imshow('read_image', image)
# # Wait to display the image until user press some key in the keyboard

# k = cv2.waitKey(0)
# # press esc key to exit
# if k == 27:
#     cv2.destroyAllWindows()
# elif k == ord('s'): # press s button to save and exit
#     cv2.imwrite('Gray_Image.png', img)
#     cv2.destroyAllWindows()

# read Video

# capture = cv2.VideoCapture('video\video.mp4')
capture = cv2.VideoCapture('D:\\Data_Science\\CV\\OpenCV_Projects\\read_images.py')

while True:
    # use Boolean to check the capture the video frame by frame
    isTrue, frame = capture.read()
    # display frame by frame in the video
    cv2.imshow('Video', frame)
    
    # to stop the video press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
capture.release()
cv2.destroyAllWindows()
