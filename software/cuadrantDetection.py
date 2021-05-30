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

def pointInterceptPointPointPointPoint(a, b, c, d):

    divide = (a[0] - b[0]) * (c[1] - d[1]) - (a[1] - b[1]) * (c[0] - d[0])
    punto1 = ((a[0]*b[1] - a[1]*b[0]) * (c[0]-d[0]) - (a[0]-b[0]) * (c[0]*d[1] - c[1]*d[0]))/divide
    punto2 = ((a[0]*b[1] - a[1]*b[0]) * (c[1]-d[1]) - (a[1]-b[1]) * (c[0]*d[1] - c[1]*d[0]))/divide
    return (int(punto1), int(punto2))

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
            P13 = pointInterceptPointPointPointPoint(P3,P15,P5,P11)
            P14 = getFractionPoint(P15, P3, 1/3 - 0.05)
            P16 = (P8[0] + 2, P8[1] - distancePointPoint(topCorner, bottomCorner) + 5)
            P17 = getFractionPoint(P16, P8, 1/3 - 0.05)
            P20 = (P5[0] + distancePointPoint(bottomCorner, rightCorner) - 10, P5[1] + distancePointPoint(P5, P4) - 13)
            P18 = pointInterceptPointPointPointPoint(P8,P16,P5,P20)
            P19 = getFractionPoint(P5, P20, 2/3 + 0.08)
            P21 = (P1[0] + distancePointPoint(P4,P5)-7, P1[1] + 16)
            P22 = getFractionPoint(P21, P8, 1/3-0.05)
            P25 = (P10[0]-35, P1[1]+20)
            P23 = pointInterceptPointPointPointPoint(P3,P25,P8,P21)
            P24 = getFractionPoint(P25, P3, 1/3)


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
            img = cv2.circle(img, P16, 2, blueColor, 5)
            img = cv2.circle(img, P17, 2, blueColor, 5)
            img = cv2.circle(img, P18, 2, blueColor, 5)
            img = cv2.circle(img, P19, 2, blueColor, 5)
            img = cv2.circle(img, P20, 2, blueColor, 5)
            img = cv2.circle(img, P21, 2, blueColor, 5)
            img = cv2.circle(img, P22, 2, blueColor, 5)
            img = cv2.circle(img, P23, 2, blueColor, 5)
            img = cv2.circle(img, P24, 2, blueColor, 5)
            img = cv2.circle(img, P25, 2, blueColor, 5)



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
            img = cv2.line(img, P6, P14,redColor,2)
            img = cv2.line(img, P2, P12,redColor,2)
            img = cv2.line(img, P8, P21,redColor,2)
            img = cv2.line(img, P3, P25,redColor,2)
            img = cv2.line(img, P10, P25,redColor,2)
            img = cv2.line(img, P1, P21,redColor,2)
            img = cv2.line(img, P2, P22,redColor,2)
            img = cv2.line(img, P9, P24,redColor,2)

            
            overlay = img.copy()
            pt1 = (150, 100)
            pt2 = (100, 200)
            pt3 = (200, 200)
            triangle_cnt = np.array( [pt1, pt2, pt3] )

            cv2.drawContours(img, [triangle_cnt], 0, (0,255,0), -1)
            C1 = [P1, P11, P12, P2]
            C1 = list(map(list, C1))
            C1 = np.array(C1)
        
            C1 = np.array([[25, 20], [30, 100], [75, 80], [10, 100]])
            contours = np.array( [ [50,50], [50,150], [150, 150], [150,50] ] )

            #x, y, w, h = 10, 10, 10, 10  # Rectangle parameters

            #cv2.rectangle(overlay, (x, y), (x+w, y+h), (0, 200, 0), -1)  # A filled rectangle
            # draw a triangle
            vertices = np.array([[480, 400], [250, 650], [600, 650]], np.int32)
            pts = vertices.reshape((-1, 1, 2))
            cv2.polylines(img, [pts], isClosed=True, color=(0, 0, 255), thickness=20)

            # fill it
            cv2.fillPoly(img, [pts], color=(0, 0, 255))            
            alpha = 0.4  # Transparency factor.

            # Following line overlays transparent rectangle over the image
            img = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)
            



    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()