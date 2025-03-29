# # Python program to explain cv2.putText() method

# importing cv2
import cv2
image = cv2.imread("open_cv/image/cat.jpg")

# font
font = cv2.FONT_HERSHEY_SIMPLEX
# orgin
org = (300, 600)
# fontScale
fontScale = 10
# Blue color in BGR
color = (255, 9, 9)
# Line thickness of 2 px
thickness = 20

# Using cv2.putText() method
image = cv2.putText( image,'OpenCV',org, font, fontScale, color, thickness, cv2.LINE_AA)

cv2.imshow("Text_Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()