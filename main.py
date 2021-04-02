import numpy as np
import cv2
import Shapes
import face

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    separationDistance = 60

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    EPoint = img.shape[1]//2,img.shape[0]//2
    DPoint = img.shape[1]//2-separationDistance,img.shape[0]//2
    FPoint = img.shape[1]//2+separationDistance,img.shape[0]//2
    BPoint = img.shape[1]//2,img.shape[0]//2-separationDistance
    HPoint = img.shape[1]//2,img.shape[0]//2+separationDistance
    APoint = img.shape[1]//2-separationDistance,img.shape[0]//2-separationDistance
    CPoint = img.shape[1]//2-separationDistance,img.shape[0]//2+separationDistance
    GPoint = img.shape[1]//2+separationDistance,img.shape[0]//2-separationDistance
    IPoint = img.shape[1]//2+separationDistance,img.shape[0]//2+separationDistance

    color = 0,255,0
    thickness = 2
    squareSize = 15

    '''
    Square locations
    A B C
    D E F
    G H I
    '''

    E = Shapes.Square(img,EPoint,squareSize,color,thickness)
    D = Shapes.Square(img,DPoint,squareSize,color,thickness)
    F = Shapes.Square(img,FPoint,squareSize,color,thickness)
    B = Shapes.Square(img,BPoint,squareSize,color,thickness)
    H = Shapes.Square(img,HPoint,squareSize,color,thickness)
    A = Shapes.Square(img,APoint,squareSize,color,thickness)
    C = Shapes.Square(img,CPoint,squareSize,color,thickness)
    G = Shapes.Square(img,GPoint,squareSize,color,thickness)
    I = Shapes.Square(img,IPoint,squareSize,color,thickness)

    E.display()
    D.display()
    F.display()
    B.display()
    H.display()
    A.display()
    C.display()
    G.display()
    I.display()

    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()