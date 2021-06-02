from time import sleep
import cv2 
import numpy as np

class Polygon:


    def __init__(self, coordinates, color):
        self.coordinates = coordinates
        self.color = (255, 255, 255)

    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color

    def setCoordinates(self, coordinates):
        self.coordinates = coordinates
    
    def paintPolygonLines(self, img):
        for i in range(len(self.coordinates)):
            img = cv2.circle(img, tuple(self.coordinates[i]), 2, (255,0,0), 5)        
            img = cv2.line(img, tuple(self.coordinates[i]), tuple(self.coordinates[(i + 1) % len(self.coordinates)]),(0,0,255),2)
    
    def fillPolygon(self, img, overlay):
        cv2.fillPoly(overlay, pts = [self.coordinates], color = self.color)