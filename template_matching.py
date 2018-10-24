# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 01:47:25 2018

@author: MD SAIF UDDIN
"""

import cv2

template = cv2.imread("C:\\Users\\SAMEER\\Desktop\\template.jpg", 0)
frame = cv2.imread("C:\\Users\\SAMEER\\Desktop\\player.jpg", 0)

cv2.imshow("FRAME", frame)
cv2.imshow("TEMPLATE", template)

result = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print(max_val, max_loc)
cv2.circle(result, max_loc, 15, 255, 2)
cv2.imshow("MATCHING", result)

cv2.waitKey(0)
cv2.destroyAllWindows()