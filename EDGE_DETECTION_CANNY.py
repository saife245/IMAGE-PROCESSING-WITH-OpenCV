# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 01:33:12 2018

@author: MD SAIF UDDIN
"""

#import numpy as np
import cv2

img = cv2.imread('C:\\Users\\SAMEER\\Desktop\\tomatoes.jpg', 1)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
res, thresh = cv2.threshold(hsv[:, :, 0], 25, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Thresh", thresh)

edges = cv2.Canny(img, 100, 70)
cv2.imshow("CAnny", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()