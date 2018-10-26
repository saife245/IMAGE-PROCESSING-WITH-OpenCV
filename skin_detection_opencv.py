# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 00:40:53 2018

@author: MD SAIF UDDIN
"""
import numpy as np
import cv2

img = cv2.imread('C:\\Users\\SAMEER\\Desktop\\face2.jpg', 1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h = hsv[:, :, 0]
s = hsv[:, :, 1]
v = hsv[:, :, 2]

hsv_split = np.concatenate((h, s, v), axis = 1)
cv2.imshow("Split hsv", hsv_split)

#put fillt on saturation channel 
ret, min_sat = cv2.threshold(s, 40, 255, cv2.THRESH_BINARY)
cv2.imshow("SAT FILTER", min_sat)

ret, max_hue = cv2.threshold(h, 15, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Hue FILTER", max_hue)

final = cv2.bitwise_and(min_sat, max_hue)
cv2.imshow("FINAL",final)
cv2.imshow("Original", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
