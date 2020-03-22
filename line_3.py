# Main motive - create a image and draw a line

import numpy as np
import cv2

pic = np.zeros((500, 500, 3), dtype = 'uint8')
# Creating multidimensional numpy array & fill it with zeros
# For filling zeros (np.zeros) function is used
# (500, 500) is the dimension of the image
# 3 is the number of channels (RBG)
# Data is stored in the form of Uint8 (unassigned 8-bit integer)

cv2.line(pic, (350, 350), (500, 350), (0, 0, 255))
# For creating a line we use (line function)
# (350, 350), (500, 350) = Co-ordiantes of line
# (0, 0, 255) value of the RGB Channels

cv2.imshow('dark', pic)
# dark = window name and pic is mutidimensional numpy array defined earlier

cv2.waitKey(0) # Allow the image to be open for a while until we start our program.
cv2.destroyAllWindows() # Destroy all windows associated with the image that we have opened.
