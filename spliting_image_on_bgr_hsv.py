# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 18:33:57 2018
________SPLITTING THE IMAGE WRT TO BGR AND HSV _______________
@author: MD SAIF UDDIN
"""

import numpy as np
import cv2

color = cv2.imread("C:\\Users\\SAMEER\\Desktop\\butterfly.jpg", 1)
cv2.imshow("Image", color)
cv2.moveWindow("Image", 0, 0)#to set  the window at corner
print(color.shape)
height, width, channels = color.shape

#spliting the image wrt to blue, green, red color
b, g, r = cv2.split(color)#split command split the image in respectice color
rgb_split = np.empty([height, width*3, 3])
rgb_split[:, 0:width] = cv2.merge([b, b, b])#as we know it is 3 channel image so blue is repeated 3times
rgb_split[:, width:width*2] = cv2.merge([g, g, g])
rgb_split[:, width*2:width*3] = cv2.merge([r, r, r])
cv2.imshow("Channels", rgb_split)
cv2.moveWindow("Channels", 0, height)

#Analysing the image wrt "Hue, Saturation and Value"
hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)#converting the bgr format to hsv
h, s, v = cv2.split(hsv)
hsv_split = np.concatenate((h, s, v), axis = 1)
cv2.imshow("Split HSV", hsv_split)

cv2.waitKey(0)
cv2.destroyAllWindows()

#ANother way of spliting the image on grey channel
color = cv2.imread("C:\\Users\\SAMEER\\Desktop\\butterfly.jpg", 1)

gray = cv2.cvtColor(color, cv2.COLOR_RGB2GRAY)#converting rgb to grey
cv2.imwrite("C:\\Users\\SAMEER\\Desktop\\butterfly_grey.jpg", gray)

b = color[:, :, 0]
g = color[:, :, 1]
r = color[:, :, 2]

#putting the alpha layer
rgba = cv2.merge((b, g, r, g))#putting 4th layer green(g) as alpha channel
cv2.imwrite("C:\\Users\\SAMEER\\Desktop\\butterfly_rgba.jpg", rgba)

