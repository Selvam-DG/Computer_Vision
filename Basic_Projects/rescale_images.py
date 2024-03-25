import cv2
import numpy as np


# rescale the images, videos, live videos

def rescaleFrame(frame, resize= 0.75):
    # frame.shape gives rows and column values
    # width of image is column size
    width = int(frame.shape[1]*resize)
    # height of image is row size
    height = int(frame.shape[0]*resize)
    
    dimension = (width,height) 
    return cv2.resize(frame, dimension, interpolation=cv2.INTER_AREA )

# To change resolutions only on live Vides
def ChangeRes(width, height):
    capture.set(3,width)
    capture.set(4,height)
    

# ## Reading images
# image = cv2.imread('D:/Data_Science/CV/OpenCV_Projects\Photos/messi.jpg')
# cv2.imshow('image', image)
# k = cv2.waitKey(0)
# if k == 27:
#     cv2.destroyAllWindows()
# elif k == ord('s'):
#     cv2.imwrite('cat_resave', image)
#     cv2.destroyAllWindows()
    
# ## Resizing the image ###
# cv2.imshow('Resize image', rescaleFrame(image))
# cv2.waitKey(0)
# cv2.destroyAllWindows()


##### Reading vieo

capture = cv2.VideoCapture(0)

if(capture.isOpened() == False):
    print("Error in opening the video file")

while True:
    # use Boolean to check the capture the video frame by frame
    isTrue, frame = capture.read()
    # display frame by frame in the video
    if isTrue == True:
        cv2.imshow('Video', frame)
        # to stop the video press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    
    # h,w = frame.shape
    # cv2.imshow('change_res', ChangeRes(h,w))
    
    
capture.release()
cv2.destroyAllWindows()