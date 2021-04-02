import cv2

'''
    Square locations
    A B C
    D E F
    G H I
'''

class Square:
    def __init__(self, img, center, width, color, thickness):
        self.img = img
        self.center = center
        self.width = width
        self.color = color
        self.thickness = thickness

    def display(self):
        cv2.rectangle(self.img, (self.center[0] - self.width, self.center[1] - self.width) ,  (self.center[0] + self.width, self.center[1] + self.width) , self.color, self.thickness)