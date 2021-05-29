import cv2
import cv2.aruco as aruco
import numpy as np
import os

def getMidPoint(a, b):
    return (int((a[0] + b[0]) / 2), int((a[1] + b[1]) / 2))

def getThirdPoint(a, b):
    return (int((a[0] + b[0]) / 3), int((a[1] + b[1]) / 3))

def getTwoThirdsPoint(a, b):
    return (int((a[0] + b[0]) * 2 / 3), int((a[1] + b[1]) * 2 / 3))

def getFractionPoint(a, b, t):
    return ( int(a[0] * (1 - t) ) + int(b[0] * t), int( a[1] * (1 - t) ) + int(b[1] * t) )

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
greenColor = (0,255,0)
blueColor = (255,0,0)
redColor = (0,0,255)
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
            img = cv2.circle(img, coords, 2, redColor, 5)
        if(howManyArucos == 2):
            topCorner = getMidPoint(coordinates[0], coordinates[1])
            topCorner = (topCorner[0]-5, topCorner[1]+25)
            bottomCorner = (topCorner[0]-5, topCorner[1]+160)
            rightCorner = (bottomCorner[0]+130, bottomCorner[1]+50)
            leftCorner = (bottomCorner[0]-130, bottomCorner[1]+45)
            img = cv2.line(img, topCorner, bottomCorner,greenColor,8)
            img = cv2.line(img, bottomCorner, rightCorner,greenColor,8)
            img = cv2.line(img, bottomCorner, leftCorner,greenColor,8)

            P1 = getFractionPoint(bottomCorner, leftCorner, 5/6)
            P2 = getFractionPoint(bottomCorner, leftCorner, 3/6)
            P3 = getFractionPoint(bottomCorner, leftCorner, 1/6)

            P1 = (P1[0] + 7, P1[1] - 30)
            P2 = (P2[0], P2[1] - 30)
            P3 = (P3[0], P3[1] - 30)

            P4 = getFractionPoint(bottomCorner, topCorner, 3/6)
            P5 = getFractionPoint(bottomCorner, topCorner, 5/6) 

            P4 = (P4[0] - 20, P4[1])
            P5 = (P5[0] - 20, P5[1])

            P6 = getFractionPoint(topCorner, bottomCorner, 1/6)
            P7 = getFractionPoint(topCorner, bottomCorner, 3/6)
            P8 = getFractionPoint(topCorner, bottomCorner, 5/6)

            P6 = (P6[0] + 25, P6[1])
            P7 = (P7[0] + 25, P7[1])
            P8 = (P8[0] + 25, P8[1] + 7)
            
            P9 = getFractionPoint(bottomCorner, rightCorner, 3/6)
            P10 = getFractionPoint(bottomCorner, rightCorner, 5/6) 

            P9 = (P9[0] + 10, P9[1] - 25)
            P10 = (P10[0], P10[1] - 25)

            P11 = getFractionPoint(bottomCorner, leftCorner, 5/6)
            P12 = getFractionPoint(bottomCorner, leftCorner, 3/6)
            P13 = bottomCorner

            P11 = (P11[0] + 30, P11[1] + 8)
            P12 = (P12[0] + 22, P12[1] + 12)
            P13 = (P13[0], P13[1] + 20)

            P14 = getFractionPoint(bottomCorner, rightCorner, 3/6)
            P15 = getFractionPoint(bottomCorner, rightCorner, 5/6) 

            P14 = (P14[0] - 25, P14[1] + 8)
            P15 = (P15[0] - 25, P15[1] + 10)

            img = cv2.circle(img, P1, 2, blueColor, 5)
            img = cv2.circle(img, P2, 2, blueColor, 5)
            img = cv2.circle(img, P3, 2, blueColor, 5)
            img = cv2.circle(img, P4, 2, blueColor, 5)
            img = cv2.circle(img, P5, 2, blueColor, 5)
            img = cv2.circle(img, P6, 2, blueColor, 5)
            img = cv2.circle(img, P7, 2, blueColor, 5)
            img = cv2.circle(img, P8, 2, blueColor, 5)
            img = cv2.circle(img, P9, 2, blueColor, 5)
            img = cv2.circle(img, P10, 2, blueColor, 5)
            img = cv2.circle(img, P11, 2, blueColor, 5)
            img = cv2.circle(img, P12, 2, blueColor, 5)
            img = cv2.circle(img, P13, 2, blueColor, 5)
            img = cv2.circle(img, P14, 2, blueColor, 5)
            img = cv2.circle(img, P15, 2, blueColor, 5)








            
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()