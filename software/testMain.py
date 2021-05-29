from motor import Motor
import time
import LCD
from time import *

def commandParser(series):
    #R U R’ U R U2 R’ U
    movements = series.split(' ')
    for move in movements:
        twoMoves = False
        directionFlag = False
        if len(move) == 2:
            if(move[1] == '2'):
                #cw cw
                twoMoves = True
            else:
                #ccw
                directionFlag = True

        if(move[0] == 'F'):
            if(twoMoves):
                F.turn90CW()
                F.turn90CW()
            else:
                F.turn90(directionFlag)
        if(move[0] == 'L'):
            if(twoMoves):
                L.turn90CW()
                L.turn90CW()
            else:
                L.turn90(directionFlag)  
        if(move[0] == 'R'):
            if(twoMoves):
                R.turn90CW()
                R.turn90CW()
            else:
                R.turn90(directionFlag)
        if(move[0] == 'B'):
            if(twoMoves):
                B.turn90CW()
                B.turn90CW()
            else:
                B.turn90(directionFlag)
        if(move[0] == 'U'):
            if(twoMoves):
                U.turn90CW()
                U.turn90CW()
            else:
                U.turn90(directionFlag)
        if(move[0] == 'D'):
            if(twoMoves):
                D.turn90CW()
                D.turn90CW()
            else:
                D.turn90(directionFlag)
        twoMoves = False
        directionFlag = False

turnDelay = .005 / 8 * 1/2

F = Motor(26,19)
L = Motor(13,6)
R = Motor(21, 20)
B = Motor(16,12)
U = Motor(5, 22)
D = Motor(27, 17)

screen = LCD.lcd()
screen.lcd_display_string("hay 6 motores", 1)

F.setDelay(turnDelay)
L.setDelay(turnDelay)
R.setDelay(turnDelay)
B.setDelay(turnDelay)
U.setDelay(turnDelay)
D.setDelay(turnDelay)

#commandParser("D U2 R D F L' D2 R' D L D' R2 B2 R2 D B2 D' B2 D2 F2")
#cube in a cube pattern
#commandParser("F L F U’ R U F2 L2 U’ L’ B D’ B’ L2 U")
#6 centers
commandParser("F2 B2 U D’ R2 L2 U D’")
'''
#test
F.turn90CW()

D.turn90CW()
U.turn90CW()
L.turn90CCW()
D.turn90CCW()
U.turn90CW()
U.turn90CW()
L.turn90CCW()
F.turn90CCW()
F.turn90CCW()
U.turn90CW()
L.turn90CCW()

time.sleep(5)

L.turn90CW()
U.turn90CCW()
F.turn90CW()
F.turn90CW()
L.turn90CW()
U.turn90CCW()
U.turn90CCW()
D.turn90CW()
L.turn90CW()
U.turn90CCW()
D.turn90CCW()
F.turn90CCW()


'''
'''
#tuning
F.turn90CW()
F.turn90CW()
F.turn90CW()
F.turn90CCW()
F.turn90CCW()
F.turn90CCW()

L.turn90CW()
L.turn90CW()
L.turn90CW()
L.turn90CCW()
L.turn90CCW()
L.turn90CCW()

R.turn90CW()
R.turn90CW()
R.turn90CW()
R.turn90CCW()
R.turn90CCW()
R.turn90CCW()


B.turn90CW()
B.turn90CW()
B.turn90CW()
B.turn90CCW()
B.turn90CCW()
B.turn90CCW()

U.turn90CW()
U.turn90CW()
U.turn90CW()
U.turn90CCW()
U.turn90CCW()
U.turn90CCW()

D.turn90CW()
D.turn90CW()
D.turn90CW()
D.turn90CCW()
D.turn90CCW()
D.turn90CCW()
'''

