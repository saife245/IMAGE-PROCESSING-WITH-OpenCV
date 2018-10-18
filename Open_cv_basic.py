# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 12:01:00 2018

______OPENCV BASIC_________________

@author: MD SAIF UDDIN
"""
#opencv work with BGR Format while MATPLOT work with RGB Format

import cv2

#loading the image
img = cv2.imread("C:\\Users\\SAMEER\\Desktop\\OpenCV_Logo.png", 1) #1 denote image is original:: if it is 0 then image is black and white

#creating the window to show the image
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

#showing the image 
cv2.imshow("Image", img)

#waiting for user to press any key to exit out
cv2.waitKey(0)

#writing the image back
cv2.imwrite("C:\\Users\\SAMEER\\Desktop\\output.png", img)