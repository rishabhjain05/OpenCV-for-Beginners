import numpy as np
import cv2

pic = np.zeros((500, 500, 3), dtype = 'uint8')
cv2.rectangle(pic, (0, 100), (500, 250), (123, 200, 98), 3, lineType = 8, shift = 0)
font = cv2.FONT_ITALIC


cv2.putText(pic, 'Rishabh', (70,250), font, 3, (255, 255, 255), 4, cv2.LINE_8)
cv2.circle(pic, (250, 250), 80, (255, 0, 255))
cv2.line(pic, (0, 350), (500, 350), (0, 0, 255))

cv2.imshow('dark', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
