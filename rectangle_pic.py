### Draw a rectangle on the image
import cv2
image = cv2.imread ("open_cv/image/cat.jpg")

# Start coordinate, here (5,5)represents the top left corner of image
start_point = (500,500)
# End coordinate, here (220, 220) represents the bottom right corner of image
end_point = (1000, 1000)
# Green color in BGR
color = (255, 0, 0)
# Line thickness of 9 px
thickness = -1

# Using cv2. rectangle() method
# Draw a rectangle with blue line borders of thickness of 2
image = cv2. rectangle( image, start_point, end_point, color, thickness)

cv2.imshow( "Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()