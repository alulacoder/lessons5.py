#### Draw a line on the image

# importing cv2
import cv2
image1 = cv2.imread ("open_cv/image/cat.jpg")

# Start coordinate, here (0,0)represents the top left corner of image
start_point = (100,100)
# End coordinate, here (250, 250) represents the bottom right corner of image
end_point = (250, 100)
# Green color in BGR
color = (0, 255, 0)
# Line thickness of 9 px
thickness = 1000

# Using cv2.line() method
# Draw a diagonal green line with thickness of 9 px
image = cv2.line(image1, start_point, end_point, color, thickness)

cv2. imshow("original", image1)
cv2. imshow ("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


