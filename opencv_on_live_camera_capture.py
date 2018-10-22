# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 20:27:04 2018

@author: MD SAIF UDDIN
"""

import cv2

cap = cv2.VideoCapture(0)# 0 for contineous
color = (0, 255, 0)
line_width = 3
radius = 100
point = (0, 0)

def click(event, x, y, flags, param):
    global point, pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Pressed", x, y)
        point = (x, y)
    
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame",click)

while(True):
    ret, frame = cap.read()#caputring each frame from video and resize it
    frame = cv2.resize(frame, (0, 0), fx = 0.5, fy = 0.5)
    cv2.circle(frame, point, radius, color, line_width)
    cv2.imshow("Frame", frame)
    
    ch = cv2.waitKey(1)#1 indicate while loop run on every 1ms 
    #to avoid stucking into while loop we use 'q' to exit out from while loop
    if ch & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()