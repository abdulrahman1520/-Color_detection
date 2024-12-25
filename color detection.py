import cv2
import cv2 as cv
import numpy as np
import time

#parameters


cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv.CAP_PROP_FRAME_HEIGHT,720)

while True :
    istrue , frame =cap.read()
    hsv_frame = cv.cvtColor(frame,cv2.COLOR_BGR2HSV)
    height , width ,_ = frame.shape
    cx = int(width/2)
    cy= int(height/2)

    #pick pixel value
    pixel_center = hsv_frame[cy,cx]
    hue_value = pixel_center[0]
    hue_value2 = pixel_center[1]
    hue_value3 = pixel_center[2]
    color = "unknown"

    if hue_value < 5 :
        color = "Red"
    elif hue_value < 5:
        color = " orange"
    elif hue_value < 33 :
        color = "yellow"
    elif hue_value < 75 :
        color = "green"
    elif hue_value < 130 :
        color = "blue"
    elif hue_value < 155 :
        color = "violet"
    elif hue_value < 165 :
        color = "pink"
    elif (hue_value & hue_value2 & hue_value3 == 0):
        color = "black"
    else :
        color = "Red"
    print(pixel_center)
    b , g , r = int(pixel_center[0]),int(pixel_center[1]),int(pixel_center[2])
    cv.putText(frame , color ,(10,50),0,1,(b,g,r),2)
    cv.circle(frame,(cx,cy),5,(b,g,r),3)

    cv.imshow("hand",frame)
    if cv.waitKey(20) & 0xFF == ord('x'):
        break

cap.release()
cv.destroyAllWindows()

