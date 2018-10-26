# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 02:06:40 2018

@author: MD SAIF UDDIN
"""

import cv2

img = cv2.imread("C:\\Users\\SAMEER\\Desktop\\face2.jpg", 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
path = "haarcascade_frontalface_default.xml"

face_cascade = cv2.CascadeClassifier(path)

faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors = 5, minSize = (40, 40))
print(len(faces))

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()