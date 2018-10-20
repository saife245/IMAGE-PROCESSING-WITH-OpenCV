# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 23:49:20 2018

@author: MD SAIF UDDIN
"""
#binary image means if the pixel is in b/w certain threshold value then it is 0(black) other wise itis 1(white)
import numpy as np
import cv2

bw = cv2.imread("C:\\Users\\SAMEER\\Desktop\\detect_blob.png", 0)
height, width = bw.shape[0:2]
cv2.imshow("Original BW", bw)

binary = np.zeros([height, width, 1], 'uint8')

thresh = 85#because of this thresold some part of image is missing

#because of two for loop it is much slower 
for row in range(0, height):
    for col in range(0, width):
        if bw[row][col] > thresh:
            binary[row][col] = 255
        
cv2.imshow("slow Binary", binary)

#we call binary threshold of opencv function, which is much faster than for loop
ret, thresh = cv2.threshold(bw, thresh, 255, cv2.THRESH_BINARY)
cv2.imshow("CV threshold", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()