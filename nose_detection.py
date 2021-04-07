import cv2
import numpy as np
import sys

eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture('WIN_20210325_11_08_24_Pro.mp4')
ds_factor = 0.5

# while True:
#
#     ret, frame = cap.read()
#     # frame = cv2.resize(frame, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     eye_rects = eye_cascade.detectMultiScale(gray, 1.3,5)
#     nose_rects = nose_cascade.detectMultiScale(gray, 1.3, 5)
#     for (x,y,w,h) in nose_rects:
#         e_c=[]
#         cv2.rectangle(frame, (x,y) , (x+w,y+h), (0,255,0), 3)
#         cv2.rectangle(frame, (x, y-h), (x + w, y+h), (0, 255, 0), 3)
#         cv2.circle(frame, (x+w//2, y-h//2), 10, (255, 0, 0), -1)
#         for (x,y,w,h) in eye_rects:
#             cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
#             e_c.append((x,y))
#         # cv2.rectangle(frame,(e_c[0]+e_c[1])/2, (x + w, y+h), (0, 255, 0), 3)
#     cv2.imshow('frame', frame)
#
#
#     c = cv2.waitKey(1)
#     if c == 27:
#         break

i=0
while 1:

    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        i+=1
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        cv2.rectangle(img,(x+w//3,y+h//3),(x+2*w//3,y+h//2), (0, 255, 0), 3)
        cv2.circle(img,(x+w//2,y+5*h//12),10,(255,255,0),-1)
        # eyes = eye_cascade.detectMultiScale(roi_gray)
        # for (ex, ey, ew, eh) in eyes:
        #     cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    print(i)
    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()


cap.release()
cv2.destroyAllWindows()

