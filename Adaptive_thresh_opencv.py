# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 00:19:58 2018

@author: MD SAIF UDDIN
"""
#adaptive thresholding is done on lightning up the image and it is important for segmentation out

import cv2

img = cv2.imread("C:\\Users\\SAMEER\\Desktop\\sudoku.jpg", 0)
cv2.imshow("Original", img)

ret, thresh_basic = cv2.threshold(img, 70, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary", thresh_basic)

thres_adapt = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow("Adaptive Threshold", thres_adapt)

cv2.waitKey(0)
cv2.destroyAllWindows()
