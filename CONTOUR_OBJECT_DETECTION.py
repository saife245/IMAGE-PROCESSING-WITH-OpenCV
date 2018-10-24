# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 01:06:12 2018

@author: MD SAIF UDDIN
"""

import cv2

img = cv2.imread('C:\\Users\\SAMEER\\Desktop\\detect_blob.png', 1)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('BINARY', thresh)

_, contours, hierarcy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img2 = img.copy()
index = -1
thickness = 4
color = (255, 0, 255)

cv2.drawContours(img2, contours, index, color, thickness)
cv2.imshow("Countours", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()