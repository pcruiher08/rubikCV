from motor import Motor
import time
turnDelay = .005 / 8 * 1

F = Motor(26,19)
L = Motor(13,6)
R = Motor(21, 20)
B = Motor(16,12)
U = Motor(5, 22)
D = Motor(27, 17)

F.setDelay(turnDelay)
L.setDelay(turnDelay)
R.setDelay(turnDelay)
B.setDelay(turnDelay)
U.setDelay(turnDelay)
D.setDelay(turnDelay)

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
time.sleep(5)
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