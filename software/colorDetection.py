import cv2
import cv2.aruco as aruco
import numpy as np
import os

def getMidPoint(a, b):
    return (int((a[0] + b[0]) / 2), int((a[1] + b[1]) / 2))

def findArucoMarkers(img, markerSize = 4, totalMarkers=250, draw=True):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(aruco, f'DICT_{markerSize}X{markerSize}_{totalMarkers}')
    arucoDict = aruco.Dictionary_get(key)
    arucoParam = aruco.DetectorParameters_create()
    corners, ids, rejected = aruco.detectMarkers(gray, arucoDict, parameters = arucoParam)
    # print(ids)
    if draw:
        aruco.drawDetectedMarkers(img, corners,ids) 
    return [corners, ids]

cap = cv2.VideoCapture(0)   
while True:
    success, img = cap.read()
    arucofound = findArucoMarkers(img)
    howManyArucos = len(arucofound[0])

    if howManyArucos!=0:
        coordinates = []
        for bbox, id in zip(arucofound[0], arucofound[1]):
            print(bbox, id)
            coords = tuple(bbox[0][0])
            print(coords)
            coordinates.append(coords)
            img = cv2.circle(img, coords, 2, (0,0,255), 5)
        if(howManyArucos == 2):
            topCorner = getMidPoint(coordinates[0], coordinates[1])
            img = cv2.line(img, (topCorner[0]-5, topCorner[1]+10), (topCorner[0]-8, topCorner[1]+190),(0,255,255),5)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()