import cv2
import cv2.aruco as aruco
import numpy as np
import os
from polygon import Polygon 
import math as m 
import LCD

matrizKociemba = []

scanState = 0



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

def calculateHSVDistance(a, b):
    dh = min(abs(b[0]-a[0]), 360-abs(b[0]-a[0])) / 180.0
    ds = abs(b[1]-a[1])
    dv = abs(b[2]-b[0]) / 255.0
    return m.sqrt(dh*dh+ds*ds+dv*dv)

def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

def pointInsidePolygon(point, polygon):
    isInsideRight = True
    isInsideLeft = True
    #print("estoy checando ", polygon, "con ", point)
    for i in range(len(polygon)):
        result = (point[1] - polygon[i][1]) * (polygon[(i + 1) % len(polygon)][0] - polygon[i][0]) - (point[0] - polygon[i][0]) * (polygon[(i + 1) % len(polygon)][1] - polygon[i][1])
        if(not (result < 0)):
            isInsideRight = False

    for i in range(len(polygon)):
        result = (point[1] - polygon[i][1]) * (polygon[(i + 1) % len(polygon)][0] - polygon[i][0]) - (point[0] - polygon[i][0]) * (polygon[(i + 1) % len(polygon)][1] - polygon[i][1])
        if(not (result > 0)):
            isInsideLeft = False

    return isInsideRight or isInsideLeft


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


def drawPolygons(img, overlay, polygons):
    for polygon in polygons:
        polygon.paintPolygonLines(img)
        polygon.fillPolygon(img, overlay)


def colorFinder(img, contours, color_ranges_HSV):
    contoursSpecial = contours.copy()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    edgee = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    #cv2.imshow('1', img)

    edge = cv2.Canny(edgee,100,200)
    #cv2.imshow("e",edge)

    rows,cols,dim = img.shape
    out = np.zeros([rows, cols, dim], dtype=np.uint8)
    acumm = mask = np.zeros((rows, cols), dtype=np.uint8)

    low_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])


    contoursFinal = []
    colors = ['A','A','A','A','A','A','A','A','A','A','A','A','A','A','A']
    maskTemp = np.zeros([rows,cols,3],np.uint8)
    for i in range(len(contoursSpecial)):
        xavg = 0
        yavg = 0
        for j in range(len(contoursSpecial[i][0])):
            xavg += contoursSpecial[i][0][j][1]
            yavg += contoursSpecial[i][0][j][0]
        xavg /= len(contoursSpecial[i][0])
        yavg /= len(contoursSpecial[i][0])
        xavg = int(xavg)
        yavg = int(yavg)
        mask = np.zeros([rows,cols],np.uint8)
        mask[xavg][yavg] = 255
        #cv2.drawContours(mask,contoursSpecial[i],-1,255,-1)
        mean = cv2.mean(hsv,mask=mask)
        temp = np.zeros([1,1,3],np.uint8)
        temp[0][0] = mean[:3]
        #print(mean)
        #cv2.drawContours(img,contoursSpecial[i],-1,[0,0,255],3)
        #cv2.drawContours(img,[aprox],-1,mean[:2],3)
        #cv2.fillPoly(img,pts = [aprox], color = mean)
        for k in range(len(color_ranges_HSV)):
            inR = cv2.inRange(temp,color_ranges_HSV[k][1],color_ranges_HSV[k][0])
            if(inR[0][0] == 255):
                #cv2.drawContours(maskTemp,[aprox],-1,mean,3)
                #contoursFinal.append([contoursSpecial[i],color_ranges_HSV[k][2]])
                colors[i] = color_ranges_HSV[k][2]
                cv2.fillPoly(maskTemp,pts = contoursSpecial[i], color = color_ranges_HSV[k][3])

    return colors


def arucoProcessing(img):
    contoursSpecial = []
    arucofound = findArucoMarkers(img)
    howManyArucos = len(arucofound[0])
    encontreDosArucos = False
    if howManyArucos!=0:
        coordinates = []
        for bbox, id in zip(arucofound[0], arucofound[1]):
            #print(bbox, id)
            coords = tuple(bbox[0][0])
            #print(coords)
            coordinates.append(coords)
            #img = cv2.circle(img, coords, 2, redColor, 5)
        if(howManyArucos == 2):
            encontreDosArucos = True
            topCorner = getMidPoint(coordinates[0], coordinates[1])
            topCorner = (topCorner[0]-5, topCorner[1]+22)
            bottomCorner = (topCorner[0]-5, topCorner[1]+170)
            rightCorner = (bottomCorner[0]+125, bottomCorner[1]+40)
            leftCorner = (bottomCorner[0]-120, bottomCorner[1]+37)

            bigLine = 3
            smallLine = 3
            #central line
            img = cv2.line(img, topCorner, bottomCorner,[0,0,0],bigLine)
            #right line
            img = cv2.line(img, bottomCorner, rightCorner,[0,0,0],bigLine)
            #left line
            img = cv2.line(img, bottomCorner, leftCorner,[0,0,0],bigLine)

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


            C1C = [np.array([P1,P11,P12,P2])]
            C2C = [np.array([P2, P12, P13, P3])]
            C3C = [np.array([P3, P13, P5, P4])]
            C4C = [np.array([P4, P5, P18, P8])]
            C5C = [np.array([P8, P18, P19, P9])]
            C6C = [np.array([P9, P19, P20, P10])]
            C7C = [np.array([P13, P14, P6, P5])]
            C8C = [np.array([P14, P15, P7, P6])]
            C9C = [np.array([P6, P7, P16, P17])]
            C10C = [np.array([P5, P6, P17, P18])]
            C11C = [np.array([P21, P1, P2, P22])]
            C12C = [np.array([P22, P2, P3, P23])]
            C13C = [np.array([P23, P3, P4, P8])]
            C14C = [np.array([P23, P8, P9, P24])]
            C15C = [np.array([P24, P9, P10, P25])]

            contoursSpecial = [C1C,C2C,C3C,C4C,C5C,C6C,C7C,C8C,C9C,C10C,C11C,C12C,C13C,C14C,C15C]


            #lineas especiales
            
            img = cv2.line(img, P5, P20,[0,0,0],smallLine)
            img = cv2.line(img, P8, P16,[0,0,0],smallLine)
            img = cv2.line(img, P10, P20,[0,0,0],smallLine)
            img = cv2.line(img, P7, P16,[0,0,0],smallLine)
            img = cv2.line(img, P6, P17,[0,0,0],smallLine)
            img = cv2.line(img, P9, P19,[0,0,0],smallLine)
            img = cv2.line(img, P3, P15,[0,0,0],smallLine)
            img = cv2.line(img, P5, P11,[0,0,0],smallLine)
            img = cv2.line(img, P1, P11,[0,0,0],smallLine)
            img = cv2.line(img, P15, P7,[0,0,0],smallLine)
            img = cv2.line(img, P6, P14,[0,0,0],smallLine)
            img = cv2.line(img, P2, P12,[0,0,0],smallLine)
            img = cv2.line(img, P8, P21,[0,0,0],smallLine)
            img = cv2.line(img, P3, P25,[0,0,0],smallLine)
            img = cv2.line(img, P10, P25,[0,0,0],smallLine)
            img = cv2.line(img, P1, P21,[0,0,0],smallLine)
            img = cv2.line(img, P2, P22,[0,0,0],smallLine)
            img = cv2.line(img, P9, P24,[0,0,0],smallLine)
    return contoursSpecial
    
cap = cv2.VideoCapture(0)   
greenColor = (0,255,0)
blueColor = (255,0,0)
redColor = (0,0,255)


color_ranges_HSV = [
    [(179, 59, 255), (0, 0, 106),"W",(0,0,255)],
    [(180, 255, 255), (159, 50, 70),"R",(4,255,255)],
    [(8, 255, 255), (0, 45, 0),"R",(4,255,255)],
    [(20, 255, 255), (9, 58, 33),"O",(19,255,255)],
    [(35, 255, 255), (25, 50, 70),"Y",(30,255,255)],
    [(120, 255, 255), (50, 90, 135),"B",(120,255,255)],
    [(89, 255, 255), (36, 50, 70),"G",(60,255,255)]
]


stagesPictures = []


'''
estado 0, esperar 5 ticks para estabilizacion
estado 1, foto y agregar al array y luego mover motores para transicion al estado 2
estado 2, foto y agregar al array y luego mover motores para transicion al estado 3
estado 3, foto y agregar al array y luego mover motores para transicion al estado 4
estado 4, foto y agregar al array y luego mover motores para transicion al estado 5
estado 5, foto y agregar al array y luego mover motores para transicion al estado 6
estado 6, foto y agregar al array y luego mover motores para transicion al estado 7
estado 7, foto y agregar al array y luego mover motores para transicion al estado 8
estado 8, foto y agregar al array y luego mover motores para transicion al estado 9
estado 9, foto y agregar al array y luego mover motores para transicion al estado 10
estado 10, kociemba y motores
'''
screen = LCD.lcd()
screen.lcd_clear()
estadoActual = 0
ticks = 0
while True:
    success, img = cap.read()
    original = img.copy()
    #img = cv2.imread("4.jpg")
    
    contoursSpecial = arucoProcessing(img)
    respuesta = colorFinder(img, contoursSpecial, color_ranges_HSV)
    rows,cols,dim = img.shape
    maskTemp = np.zeros([rows,cols,3],np.uint8)
    for i in range(len(respuesta)):
        for j in range(len(color_ranges_HSV)):
            if(respuesta[i] == color_ranges_HSV[j][2]):
                cv2.fillPoly(maskTemp,pts = contoursSpecial[i], color = color_ranges_HSV[j][3])
    maskTemp = cv2.cvtColor(maskTemp, cv2.COLOR_HSV2BGR)
    cv2.imshow("color reconstruction",maskTemp)
    cv2.imshow("original image",original)


    if(estadoActual == 0):
        ticks += 1
        if(ticks > 5):
            estadoActual = 1
            ticks = 0
    elif(estadoActual == 1):
        if(ticks == 0):
            stagesPictures.append(original.copy())
            screen.lcd_clear()
            screen.lcd_display_string("estado 1", 1)
            #motores

        ticks += 1
        if(ticks > 10):
            estadoActual = 2
            ticks = 0
    elif(estadoActual == 2):
        if(ticks == 0):
            stagesPictures.append(original.copy())
            screen.lcd_clear()
            screen.lcd_display_string("estado 2", 1)
            #motores
        ticks += 1
        if(ticks > 10):
            estadoActual = 3
            ticks = 0
            
    elif(estadoActual == 3):
        if(ticks == 0):
            stagesPictures.append(original.copy())
            screen.lcd_clear()
            screen.lcd_display_string("estado 3", 1)
            #motores
        ticks += 1
        if(ticks > 10):
            estadoActual = 4
            ticks = 0
            
    elif(estadoActual == 4):
        if(ticks == 0):
            stagesPictures.append(original.copy())
            screen.lcd_clear()
            screen.lcd_display_string("estado 4", 1)
            #motores
        ticks += 1
        if(ticks > 10):
            estadoActual = 5
            ticks = 0
            
    elif(estadoActual == 5):
        if(ticks == 0):
            stagesPictures.append(original.copy())
            screen.lcd_clear()
            screen.lcd_display_string("estado 5", 1)
            #motores
        ticks += 1
        if(ticks > 10):
            estadoActual = 6
            ticks = 0
            
    elif(estadoActual == 6):
        if(ticks == 0):
            stagesPictures.append(original.copy())
            screen.lcd_clear()
            screen.lcd_display_string("estado 6", 1)
            #motores
        ticks += 1
        if(ticks > 10):
            estadoActual = 7
            ticks = 0
            
    elif(estadoActual == 7):
        if(ticks == 0):
            stagesPictures.append(original.copy())
            screen.lcd_clear()
            screen.lcd_display_string("estado 7", 1)
            #motores
        ticks += 1
        if(ticks > 10):
            estadoActual = 8
            ticks = 0
            
    elif(estadoActual == 8):
        if(ticks == 0):
            stagesPictures.append(original.copy())
            screen.lcd_clear()
            screen.lcd_display_string("estado 8", 1)
            #motores
        ticks += 1
        if(ticks > 10):
            estadoActual = 9
            ticks = 0
            
    elif(estadoActual == 9):
        if(ticks == 0):
            stagesPictures.append(original.copy())
            screen.lcd_clear()
            screen.lcd_display_string("estado 9", 1)
            #motores
        ticks += 1
        if(ticks > 10):
            estadoActual = 10
            ticks = 0
    elif(estadoActual == 10):
        break
        
    cv2.imshow('arucos',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break  


    #sacamos el arreglo con la letra mas repetida
    #escribimos en la matriz kociemba
    #cambiamos de estado moviendo motores y es ciclo








#cap.release()
cv2.destroyAllWindows()