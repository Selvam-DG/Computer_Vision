# # import packages
import numpy as np
import cv2

# #create a black image
# img = np.zeros((512,512,3), np.uint8)
# ### Argument in blue channel goes like B, G, R but we read as RGB

# # Draw  a diagonaö blue line with thickness of 5 pixels
# cv2.line(img, (0,0), (511,511), (255,255,255), 5)

# # Draw a rectangleq
# cv2.rectangle(img, (384,0), (510,128), (0,255,0), 3)

# # Draw a circle
# cv2.circle(img, (447,63), 63, (0,120,255), 5)

# # Draw a polygon
# pts = np.array([[0,0], [150,111], [233,250],[100, 290]])
# pts = pts.reshape((-1,1,2))
# cv2.polylines(img, [pts], True, (0,0,255), 6) # red color polygon
 
# cv2.imshow('Sample_Image', img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# use the function cv2.imread() to read an image
# cv2.IMREAD_COLOR
# cv2.IMREAD.GRAYSCALE : Load image in graysclae
# cv2.IMREAD_UNCHANGED: Load  image as such including alpha channel
# instead we can pass 1 to read image in color format, 0 to read in grayscale


img = cv2.imread("Car.jpg",1)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('image',  img)
k = cv2.waitKey(0)
if k == 27: #press esc key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # press s button to save and exit
    cv2.imwrite('Gray_Image.png', img)
    cv2.destroyAllWindows()
    
    
    
print(type(img) ,img.shape)