import numpy as np
import cv2

pic = np.zeros((500, 500, 3), dtype = 'uint8')
# a multi dimensional array is created and filled with zeros (np.zeros)
# (500, 500) image dimension and 3 = 3 channels for image (Red, Blue, Green)
# since image pixel are ranging from 0 to 255, So the data is stored in the form of Uint8 (unassigned 8-bit integer)

cv2.rectangle(pic, (0,0), (500, 150), (123, 200, 98), 3, lineType = 8, shift = 0)
# To draw a rectangle we use rectangle function
# (0,0) (500,150) = coordiantes from where you want to draw rectangle
# (123, 200, 98) = Value of RGB channel
# 3 = Number of channels
# lineType = dotted, plane etc. (*case sensitive = keyword)
# shift = will shift figure(and dimnish) 0 = max and 1,2,3.. decreasing in size

cv2.imshow('dark', pic)
# dark = window name and pic is mutidimensional numpy array defined earlier.

cv2.waitKey(0) # Allow the image to be open for a while until we start our program.
cv2.destroyAllWindows() # Destroy all windows associated with the image that we have opened.
