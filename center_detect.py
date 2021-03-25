import cv2
import numpy as np

green_range = np.array([[50,50,50],[80,255,255]])
g_area = [100,1700]
kernel = np.ones((7,7),np.uint8)

def swap( array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def makeMask(hsv_frame, color_Range):
    
    mask = cv2.inRange( hsv_frame, color_Range[0], color_Range[1])
    # Morphosis next ...
    eroded = cv2.erode( mask, kernel, iterations=1)
    dilated = cv2.dilate( eroded, kernel, iterations=1)
    
    return dilated

def drawCentroid(vid, color_area, mask):
    
    contour, _ = cv2.findContours( mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    l=len(contour)
    area = np.zeros(l)

    # filtering contours on the basis of area rane specified globally 
    for i in range(l):
        if cv2.contourArea(contour[i])>color_area[0] and cv2.contourArea(contour[i])<color_area[1]:
            area[i] = cv2.contourArea(contour[i])
        else:
            area[i] = 0
    
    a = sorted( area, reverse=True) 

    # bringing contours with largest valid area to the top
    for i in range(l):
        for j in range(1):
            if area[i] == a[j]:
                swap( contour, i, j)

    if l > 0 :      
        # finding centroid using method of 'moments'
        M = cv2.moments(contour[0])
        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            center = (cx,cy)
            cv2.circle( vid, center, 5, (0,0,255), -1)
                    
            return center
    else:
        # return error handling values
        return (-1,-1)
cap = cv2.VideoCapture('WIN_20210325_11_08_24_Pro.mp4')

cv2.namedWindow('Frame')
while(1):
    k = cv2.waitKey(10) & 0xFF
    _, frameinv = cap.read()
    # flip horizontaly to get mirror image in camera
    frame = cv2.flip( frameinv, 1)

    hsv = cv2.cvtColor( frame, cv2.COLOR_BGR2HSV)
    g_mask = makeMask( hsv, green_range)
    g_cen = drawCentroid(frame, g_area, g_mask)
    cv2.imshow('Frame', frame)
    if k == 27:
        break
cv2.destroyAllWindows()
