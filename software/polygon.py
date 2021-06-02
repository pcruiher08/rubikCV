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

    def nextColor(self):
        print("cambiando color")
        self.colorIndex = (self.colorIndex + 1) % 6
        self.color = self.colors[self.colorIndex][0]
        self.color = (255,0,0)
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