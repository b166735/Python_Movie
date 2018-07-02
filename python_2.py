import numpy as np
from scipy.ndimage.filters import convolve
from numpy import uint8, float32, float64, log, pi, sin, cos, abs, sqrt
import cv2

def myfunc(i):
    pass

cv2.namedWindow('camera')
cv2.createTrackbar('gamma','camera',0,500,myfunc)
cv2.createTrackbar("R","camera",1,10,myfunc)
cv2.createTrackbar("G","camera",1,10,myfunc)
cv2.createTrackbar("B","camera",1,10,myfunc)
cv2.createTrackbar("ON/OFF","camera",0,1,myfunc)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while(True):
    ret, frame = cap.read()
    if not ret: continue
    v = cv2.getTrackbarPos('gamma','camera')
    r = cv2.getTrackbarPos("R", "camera")
    g = cv2.getTrackbarPos("G", "camera")
    b = cv2.getTrackbarPos("B", "camera")
    sw= cv2.getTrackbarPos("ON/OFF","camera")
    lf=np.array([[0,1,0],
                [1,-4,1],
                [0,1,0]])
    gframe=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


    B=frame[:,:,0]
    G=frame[:,:,1]
    R=frame[:,:,2]
    R=R/255.0
    G=G/255.0
    B=B/255.0

    R=(R**(v/100.0))
    G=(G**(v/100.0))
    B=(B**(v/100.0))

    if r!=0:
        R=(R**(1/r))
    if g!=0:
        G=(G**(1/g))
    if b!=0:
        B=(B**(1/b))

    if sw==1:
        lframe=convolve(gframe,lf)
        frame=lframe
        frame=frame.astype(np.uint8)
    else:
        frame[:,:,0]=255.0*B
        frame[:,:,1]=255.0*G
        frame[:,:,2]=255.0*R

    cv2.imshow('camera', frame)
    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break

cap.release()
cv2.destroyAllWindows()
