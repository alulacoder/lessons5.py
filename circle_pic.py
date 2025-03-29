#### Draw the circle on the image

import cv2
image = cv2.imread ("open_cv/image/cat.jpg")

# Center coordinates 
center_coordinates = (750,700)
# Radius of circle
radius = 200
# Blue color in BGR
color =(255, 0, 0)
# Line thickness of 2 px
thickness = -1

# Using cv2.circle() method
# Draw a circle with blue line borders of thickness of 2 px
image = cv2.circle(image, center_coordinates, radius, color, thickness)

# Displaying the
image
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()