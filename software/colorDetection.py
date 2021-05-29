import cv2
import cv2.aruco as aruco
import numpy as np
import os
def findArucoMarkers(img, markerSize = 4, totalMarkers=250, draw=True):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(aruco, f'DICT_{markerSize}X{markerSize}_{totalMarkers}')
    arucoDict = aruco.Dictionary_get(key)
    arucoParam = aruco.DetectorParameters_create()
    bboxs, ids, rejected = aruco.detectMarkers(gray, arucoDict, parameters = arucoParam)
    # print(ids)
    if draw:
        aruco.drawDetectedMarkers(img, bboxs,ids) 
    return [bboxs, ids]

cap = cv2.VideoCapture(2)   
while True:
    success, img = cap.read()
    arucofound = findArucoMarkers(img)
    if  len(arucofound[0])!=0:
        for bbox, id in zip(arucofound[0], arucofound[1]):
            print(bbox, id)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()