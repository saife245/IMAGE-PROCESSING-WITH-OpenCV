# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 19:59:44 2018

@author: MD SAIF UDDIN
"""

import cv2

img = cv2.imread("C:\\Users\\SAMEER\\Desktop\\player.jpg")

#scale
img_half = cv2.resize(img, (0, 0), fx = 0.5,fy = 0.5)
img_stretch = cv2.resize(img, (720, 600))
img_stretch_near = cv2.resize(img, (720, 600), interpolation = cv2.INTER_NEAREST)
#interpolation technique that reduce the visual distortion caused by fractional zoom

cv2.imshow("HALF", img_half)
cv2.imshow("STRETCH", img_stretch)
cv2.imshow("STRETCH_NEAR", img_stretch_near)

#rotaion
M = cv2.getRotationMatrix2D((0, 0), -30, 1)
rotated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow("ROTATED", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
