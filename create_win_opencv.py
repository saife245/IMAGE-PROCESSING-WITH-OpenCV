# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 12:12:18 2018

++++ BY USING NUMPY AND OPENCV WE CREATE WINDOW OF DIFFERENT BGR COLOR+++++++++
HERE ON OPENCV WE USE BGR FORMAT OF COLOR

@author: MD SAIF UDDIN
"""

import numpy as np
import cv2

#creating the black window
black = np.zeros([150, 200, 1], 'uint8')
cv2.imshow("Black", black)
print(black[0, 0, :])

#creating the other window by using the ones function
ones = np.ones([150, 200, 1], 'uint8')
cv2.imshow("Ones", ones)
print(ones[0, 0, :])

#creating the white background window
color = np.ones([150, 200, 3], 'uint16')
color = color * (2**16 - 1)
cv2.imshow("colors", color)
print(color[0,0, :])

cv2.waitKey(0)
cv2.destroyAllWindows()