# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 19:15:31 2018

Analysis the image with GAUSSIAN BLUR, DILATE and ERODE

@author: MD SAIF UDDIN
"""
#Dilate convert black pixel to white pixel
#Erode convert white pixel to black pixel

import cv2
import numpy as np

image = cv2.imread("C:\\Users\\SAMEER\\Desktop\\butterfly.jpg")
cv2.imshow("Original", image)

blur = cv2.GaussianBlur(image, (5, 25), 0)#(5, 55) represent the value on x and y axis where blur occur and take both odd dimension value
cv2.imshow("Blur", blur)

kernel = np.ones((5, 5), 'uint8')

dilate = cv2.dilate(image, kernel, iterations = 1)
erode = cv2.erode(image, kernel, iterations = 1)

cv2.imshow("Dilate", dilate)
cv2.imshow("Erode", erode)

cv2.waitKey(0)
cv2.destroyAllWindows()

