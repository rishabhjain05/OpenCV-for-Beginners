import numpy as np
import cv2

pic = np.zeros((500, 500, 3), dtype = 'uint8')
# Creating multidimensional numpy array & fill it with zeros
# For filling zeros (np.zeros) function is used
# (500, 500) is the dimension of the image
# 3 is the number of channels (RBG)
# Data is stored in the form of Uint8 (unassigned 8-bit integer)

color = (255, 0, 255)
# Value of channels(RBG)

cv2.circle(pic, (250, 250), 80, color)
# For creating a circle we use (circle function)
# (250, 250) = center of the circle
# 80 = radius of the circle
# color is a function containg the value of channels(RBS)
# Can alos be written as cv2.circle(pic, (250, 250), 80, (255, 0, 255))

cv2.imshow('dark', pic)
# dark = window name and pic is mutidimensional numpy array defined earlier.

cv2.waitKey(0) # Allow the image to be open for a while until we start our program.
cv2.destroyAllWindows() # Destroy all windows associated with the image that we have opened.
