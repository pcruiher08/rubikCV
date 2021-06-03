from time import sleep
import cv2 
import numpy as np

class Polygon:
    #blanco, azul, verde, rojo, amarillo, naranja
    colors = [[(255,255,255),'W'],
              [(255,0,0),'B'],
              [(0,255,0),'G'],
              [(0,0,255),'R'],
              [(255,255,0),'Y'],
              [(255,169,0),'O']
                ]

    def __init__(self, coordinates, color):
        self.colors = [[(255,255,255),'W'],
              [(255,0,0),'B'],
              [(0,255,0),'G'],
              [(0,0,255),'R'],
              [(255,255,0),'Y'],
              [(255,169,0),'O']
                ]
        self.coordinates = coordinates
        self.color = color
        self.colorIndex = 0
        self.colorLetter = self.colors[self.colorIndex][1]

    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def getColorLetter(self):
        return self.colorLetter

    def getCentroid(self):
        avgX = 0
        avgY = 0

        for point in self.coordinates:
            avgX += point[0]
            avgY += point[1]
        
        avgX /= len(self.coordinates)
        avgY /= len(self.coordinates)

        return (avgX, avgY)

    def nextColor(self):
        print("cambiando color")
        self.colorIndex = (self.colorIndex + 1) % 6
        self.color = self.colors[self.colorIndex][0]
        self.color = (255,0,0)
        print(self.colorLetter)

    def setCoordinates(self, coordinates):
        self.coordinates = coordinates

    def getCoordinates(self):
        return self.coordinates
    
    def paintPolygonLines(self, img):
        for i in range(len(self.coordinates)):
            img = cv2.circle(img, tuple(self.coordinates[i]), 2, (255,0,0), 5)        
            img = cv2.line(img, tuple(self.coordinates[i]), tuple(self.coordinates[(i + 1) % len(self.coordinates)]),(0,0,255),2)
    
    def fillPolygon(self, img, overlay):
        cv2.fillPoly(overlay, pts = [self.coordinates], color = self.color)

    '''
    
            C1 = Polygon(np.array(list(map(list, [P1, P11, P12, P2]))), (255,255,255)) 
            C2 = Polygon(np.array(list(map(list, [P2, P12, P13, P3]))), (255,255,255))
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
    '''