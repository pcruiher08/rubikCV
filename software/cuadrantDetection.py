import cv2
import cv2.aruco as aruco
import numpy as np
import os
import math as m 

def getMidPoint(a, b):
    return (int((a[0] + b[0]) / 2), int((a[1] + b[1]) / 2))

def getThirdPoint(a, b):
    return (int((a[0] + b[0]) / 3), int((a[1] + b[1]) / 3))

def getTwoThirdsPoint(a, b):
    return (int((a[0] + b[0]) * 2 / 3), int((a[1] + b[1]) * 2 / 3))

def getFractionPoint(a, b, t):
    return ( int(a[0] * (1 - t) ) + int(b[0] * t), int( a[1] * (1 - t) ) + int(b[1] * t) )

def distancePointPoint(a, b):
    return int( m.sqrt( (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]) ) )

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
            topCorner = (topCorner[0]-5, topCorner[1]+22)
            bottomCorner = (topCorner[0]-5, topCorner[1]+170)
            rightCorner = (bottomCorner[0]+125, bottomCorner[1]+40)
            leftCorner = (bottomCorner[0]-120, bottomCorner[1]+37)

            #central line
            img = cv2.line(img, topCorner, bottomCorner,greenColor,8)
            #right line
            img = cv2.line(img, bottomCorner, rightCorner,greenColor,8)
            #left line
            img = cv2.line(img, bottomCorner, leftCorner,greenColor,8)

            P1 = leftCorner
            P2 = getFractionPoint(bottomCorner, leftCorner, 2/3)
            P3 = getFractionPoint(bottomCorner, leftCorner, 1/3)
            P4 = bottomCorner
            P5 = getFractionPoint(bottomCorner, topCorner, 1/3+0.05) 
            P6 = getFractionPoint(bottomCorner, topCorner, 2/3+0.05)
            P7 = topCorner
            P8 = getFractionPoint(bottomCorner, rightCorner, 1/3 + 0.05)
            P9 = getFractionPoint(bottomCorner, rightCorner, 2/3 + 0.05)
            P10 = rightCorner 
            P11 = (P1[0]+8, P1[1] - distancePointPoint(P4, P5)+10) 
            P12 = getFractionPoint(P11, P5, 1/3)



            P15 = (P3[0]+7, P3[1] - distancePointPoint(bottomCorner, topCorner)+7)
            P14 = getFractionPoint(P15, P3, 1/3 - 0.05)

            P16 = (P8[0] + 2, P8[1] - distancePointPoint(topCorner, bottomCorner) + 5)
            P17 = getFractionPoint(P16, P8, 1/3 - 0.05)


            P20 = (P5[0] + distancePointPoint(bottomCorner, rightCorner) - 10, P5[1] + distancePointPoint(P5, P4) - 13)
            P19 = getFractionPoint(P5, P20, 2/3 + 0.08)

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



            img = cv2.circle(img, P14, 2, blueColor, 5)
            img = cv2.circle(img, P15, 2, blueColor, 5)
            img = cv2.circle(img, P16, 2, blueColor, 5)
            img = cv2.circle(img, P17, 2, blueColor, 5)

            img = cv2.circle(img, P19, 2, blueColor, 5)
            img = cv2.circle(img, P20, 2, blueColor, 5)


            #lineas especiales

            img = cv2.line(img, P5, P20,redColor,2)
            img = cv2.line(img, P8, P16,redColor,2)
            img = cv2.line(img, P10, P20,redColor,2)

            img = cv2.line(img, P7, P16,redColor,2)
            img = cv2.line(img, P6, P17,redColor,2)

            img = cv2.line(img, P9, P19,redColor,2)
            img = cv2.line(img, P3, P15,redColor,2)
            img = cv2.line(img, P5, P11,redColor,2)
            img = cv2.line(img, P1, P11,redColor,2)
            img = cv2.line(img, P15, P7,redColor,2)





            
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()