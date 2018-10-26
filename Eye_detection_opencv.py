# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 02:21:13 2018

@author: MD SAIF UDDIN
"""

import cv2

img = cv2.imread("C:\\Users\\SAMEER\\Desktop\\face2.jpg", 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
path = "haarcascade_eye.xml"

eye_cascade = cv2.CascadeClassifier(path)

eyes = eye_cascade.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors = 20, minSize = (10, 10))
print(len(eyes))

for (x, y, w, h) in eyes:
    xc = (x + x+w)/2
    yc = (y + y+h)/2
    radius = w/2
    cv2.circle(img, (int(xc),int(yc)), int(radius), (255, 0, 0), 2)
cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()