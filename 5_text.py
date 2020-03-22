import numpy as np
import cv2

pic = np.zeros((500, 500, 3), dtype = 'uint8')
# Creating multidimensional numpy array & fill it with zeros
# For filling zeros (np.zeros) function is used
# (500, 500) is the dimension of the image
# 3 is the number of channels (RBG)
# Data is stored in the form of Uint8 (unassigned 8-bit integer)

font = cv2.FONT_ITALIC
# We need to define a font.
# Here font is FONT_ITALIC
# More types of font can be found in OpenCV documentation

cv2.putText(pic, 'Rishabh', (70,250), font, 3, (255, 255, 255), 4, cv2.LINE_8)
# Function cv2.putText, this will help us to write on image.
# pic = picture on which we are going to write text.
# Rishabh = The text you want to write on image.
# (70,250) = Co-ordinates of text on picture.
# font = The style of font that is defined earlier, before main function.
# 3 = size of overall text.
# (255, 255, 255) = value for the RGB channels.
# 4 = Thickness of the text.
# cv2.LINE_8 = Type of line used to draw text.

cv2.imshow('dark', pic)
# dark = window name and pic is mutidimensional numpy array defined earlier.

cv2.waitKey(0) # Allow the image to be open for a while until we start our program.
cv2.destroyAllWindows() # Destroy all windows associated with the image that we have opened.
