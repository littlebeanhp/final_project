import cv2
import numpy as np
import dlib


cap = cv2.VideoCapture('WIN_20210325_11_08_24_Pro.mp4')
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
from pandas import DataFrame
#
# cv2.destroyAllwindows()
# cv2.waitKey(0)

while(True):
    # Capture frame-by-frame
    ret, frameinv = cap.read()
    frame = cv2.flip(frameinv, 1)
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        cv2.rectangle(frame, (x1+20, y1-20), (x2-20, y2), (0, 255, 0), 2)
        landmarks = predictor(gray, face)
        # for n in range(0, 68):
        #     x = landmarks.part(n).x
        #     y = landmarks.part(n).y
        #     cv2.circle(frame, (x, y), 4, (255, 0, 0), -1)

        x=landmarks.part(27).x
        y=landmarks.part(27).y
        cv2.circle(frame, (x, y), 10, (255, 0, 0), -1)
        df = DataFrame({'X-axis': x, 'Y-axis': y})
        df.to_excel('test.xlsx', sheet_name='sheet1', index=False)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


#tin hieu o vung tran se la cuc dai
#==điểm 28
#thiết lập bộ đọc đo vị trí mặt nghiêng lấy tâm là đường ngang đi qua ấn đường kẻ grid trên mặt ảnh sai lệch bao nhiêu
#loại tin hiệu thông cao

