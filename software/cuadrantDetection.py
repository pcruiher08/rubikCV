import cv2
import cv2.aruco as aruco
import numpy as np
import os
from polygon import Polygon 
import math as m 

def rgb_to_hsv(r, g, b):
    return r, g, b
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
    v = mx*100
    return h, s, v

def mouseRGB(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
        colorsB = frame[y,x,0]
        colorsG = frame[y,x,1]
        colorsR = frame[y,x,2]
        colors = frame[y,x]
        #print("Red: ",colorsR)
        #print("Green: ",colorsG)
        #print("Blue: ",colorsB)
        #print("BRG Format: ",colors)
        #print("Coordinates of pixel: X: ",x,"Y: ",y)
        print(rgb_to_hsv(colorsR,colorsG,colorsB))

availalePolygons = []
'''
def clickInPolygon(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
        for polygon in availalePolygons:
            if(pointInsidePolygon((x,y), polygon)):
'''

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
    isInside = True
    for i in range(len(polygon)):
        result = (point[1] - polygon[i][1]) * (polygon[(i + 1) % len(polygon)][0] - polygon[i][0]) - (point[0] - polygon[i][0]) * (polygon[(i + 1) % len(polygon)][1] - polygon[i][1])
        if(not (result < 0)):
            isInside = False
    if(isInside):
        print("toi adentro bro")
    else:
        print("ando aca afuera, abreme")
    return isInside

def getAverageInsidePolygon(img, polygon):
    imghsv = img.copy()
    imghsv = cv2.cvtColor(imghsv, cv2.COLOR_BGR2RGB)
    mask = np.zeros(img.shape[:2], dtype = np.uint8)
    cv2.fillPoly(mask, pts = [polygon], color = (255,255,255))
    average = cv2.mean(imghsv,mask=mask)[:3]
    color_ranges_RGB= [
    [(180, 180, 230),"W"],
    [(255, 169, 0),"O"],
    [(0, 255, 0),"G"],
    [(255, 0, 0),"R"],
    [(255, 255, 0),"Y"],
    [(20, 150, 255),"B"]]
    '''
    color_ranges_HSV = [
    [(234, 8, 255),"W"],
    [(30, 63, 255),"O"],
    [(127, 58, 131),"G"],
    [(8, 70, 131),"R"],
    [(60, 47, 189),"Y"],
    [(209, 90, 255),"B"]]
    '''
    '''
    color_ranges_HSV = [
    [(55, 0, 161), (210, 17, 255),"W"],
    [(13, 53, 255), (43, 68, 255),"O"],
    [(127, 58, 131), (143, 83, 233),"G"],
    [(8, 70, 131), (17, 100, 250),"R"],
    [(60, 47, 189), (66, 65, 255),"Y"],
    [(55, 0, 161), (210, 17, 255),"B"]]
    '''
    '''
    color_ranges_HSV = [
    [(180, 18, 255), (0, 0, 231),"W"],
    [(24, 255, 255), (10, 50, 70),"O"],
    [(89, 255, 255), (36, 50, 70),"G"],
    [(180, 255, 255), (159, 50, 70),"R"],
    [(9, 255, 255), (0, 50, 70),"R"],
    [(35, 255, 255), (25, 50, 70),"Y"],
    [(128, 255, 255), (90, 50, 70),"B"]]
    '''

    nearestColor = 'P'
    minimumDistance = 1000
    for color in color_ranges_RGB:
        comparison1 = calculateHSVDistance(color[0], average)
        #comparison2 = calculateHSVDistance(color[1], average)
        #closestColor = min(comparison1, comparison2)
        closestColor = comparison1
        if( closestColor < minimumDistance ):
            minimumDistance = closestColor
            nearestColor = color[1]

    if(nearestColor == 'W'):
        average = (255,255,255)
    elif(nearestColor == 'R'):
        average = (0,0,255)
    elif(nearestColor == 'G'):
        average = (0,255,0)
    elif(nearestColor == 'B'):
        average = (255,0,0)
    elif(nearestColor == 'Y'):
        average = (0,255,255)
    elif(nearestColor == 'O'):
        average = (0,128,255)

    #print(nearestColor, namestr(polygon, globals()))
    return average, nearestColor

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



cv2.namedWindow('mouseRGB')
cv2.setMouseCallback('mouseRGB',mouseRGB)

cap = cv2.VideoCapture(0)   
greenColor = (0,255,0)
blueColor = (255,0,0)
redColor = (0,0,255)




while True:
    success, img = cap.read()
    frame = img.copy()
    arucofound = findArucoMarkers(img)
    howManyArucos = len(arucofound[0])

    if howManyArucos!=0:
        coordinates = []
        for bbox, id in zip(arucofound[0], arucofound[1]):
            #print(bbox, id)
            coords = tuple(bbox[0][0])
            #print(coords)
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
            overlay = img.copy()


            C1 = np.array(list(map(list, [P1, P11, P12, P2])))

            C1 = Polygon(np.array(list(map(list, [P1, P11, P12, P2]))), (255,255,255)) 


            polygons = []
            polygons.append(C1)



            alpha = 0.5

            drawPolygons(img, overlay, polygons)
            cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0, img)


            '''
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

            C1 = np.array(list(map(list, [P1, P11, P12, P2])))
            C2 = np.array(list(map(list, [P2, P12, P13, P3])))
            C3 = np.array(list(map(list, [P3, P13, P5, P4])))
            C4 = np.array(list(map(list, [P4, P5, P18, P8])))
            C5 = np.array(list(map(list, [P8, P18, P19, P9])))
            C6 = np.array(list(map(list, [P9, P19, P20, P10])))
            C7 = np.array(list(map(list, [P13, P14, P6, P5])))
            C8 = np.array(list(map(list, [P14, P15, P7, P6])))
            C9 = np.array(list(map(list, [P6, P7, P16, P17])))
            C10 = np.array(list(map(list, [P5, P6, P17, P18])))
            C11 = np.array(list(map(list, [P21, P1, P2, P22])))
            C12 = np.array(list(map(list, [P22, P2, P3, P23])))
            C13 = np.array(list(map(list, [P23, P3, P4, P8])))
            C14 = np.array(list(map(list, [P23, P8, P9, P24])))
            C15 = np.array(list(map(list, [P24, P9, P10, P25])))



            
            cv2.fillPoly(overlay, pts = [C1], color =tuple(getAverageInsidePolygon(img,C1)[0]))
            cv2.fillPoly(overlay, pts = [C2], color =tuple(getAverageInsidePolygon(img,C2)[0]))
            cv2.fillPoly(overlay, pts = [C3], color =tuple(getAverageInsidePolygon(img,C3)[0]))
            cv2.fillPoly(overlay, pts = [C4], color =tuple(getAverageInsidePolygon(img,C4)[0]))
            cv2.fillPoly(overlay, pts = [C5], color =tuple(getAverageInsidePolygon(img,C5)[0]))
            cv2.fillPoly(overlay, pts = [C6], color =tuple(getAverageInsidePolygon(img,C6)[0]))
            cv2.fillPoly(overlay, pts = [C7], color =tuple(getAverageInsidePolygon(img,C7)[0]))
            cv2.fillPoly(overlay, pts = [C8], color =tuple(getAverageInsidePolygon(img,C8)[0]))
            cv2.fillPoly(overlay, pts = [C9], color =tuple(getAverageInsidePolygon(img,C9)[0]))
            cv2.fillPoly(overlay, pts = [C10], color =tuple(getAverageInsidePolygon(img,C10)[0]))
            cv2.fillPoly(overlay, pts = [C11], color =tuple(getAverageInsidePolygon(img,C11)[0]))
            cv2.fillPoly(overlay, pts = [C12], color =tuple(getAverageInsidePolygon(img,C12)[0]))
            cv2.fillPoly(overlay, pts = [C13], color =tuple(getAverageInsidePolygon(img,C13)[0]))
            cv2.fillPoly(overlay, pts = [C14], color =tuple(getAverageInsidePolygon(img,C14)[0]))
            cv2.fillPoly(overlay, pts = [C15], color =tuple(getAverageInsidePolygon(img,C15)[0]))

            '''



    #cv2.setMouseCallback('img',clickInPolygon)

    cv2.imshow('img',img)

    cv2.imshow('mouseRGB', frame)
    cv2.imwrite('fotoparahumberto.jpg', frame)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()