#!/usr/env python 
import numpy as np
import cv2
#nuevo comentario 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture(0)
 
while(True):
    ret, img = cap.read()
 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
 
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(125,255,0),2)
 
    cv2.imshow('img',img)
     
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2-destroyAllWindows()
print 'new line'
print 'new line'
