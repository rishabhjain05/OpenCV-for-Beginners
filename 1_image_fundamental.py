import numpy as np
import cv2

img = cv2.imread('supreme.jpg', 1)
# 0 for grayscale and -1 for alpha channel.
# If image is located inside a folder use / to traverse to folder in file address.
# eg - 'C:/Users/risha/OneDrive/Desktop/supreme.jpg'

img = cv2.imwrite('sup.png', img)
# To write the image in another format (jpg to png).

cv2.imshow('original', img)
#cv2.imshow will provide your name to pop up window.

cv2.waitKey(0) # Allow the image to be open for a while until we start our program.
cv2.destroyAllWindows() # Destroy all windows associated with the image that we have opened.
