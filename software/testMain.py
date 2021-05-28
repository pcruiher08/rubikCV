from motor import Motor


F = Motor(26,19)
L = Motor(13,6)
R = Motor(21, 20)
B = Motor(16,12)
U = Motor(5, 22)


F.setDelay(.005 / 8 * 1)
F.turn90CW()
F.turn90CW()
F.turn90CW()
F.turn90CCW()
F.turn90CCW()
F.turn90CCW()


L.setDelay(.005 / 8 * 1)
L.turn90CW()
L.turn90CW()
L.turn90CW()
L.turn90CCW()
L.turn90CCW()
L.turn90CCW()


R.setDelay(.005 / 8 * 1)
R.turn90CW()
R.turn90CW()
R.turn90CW()
R.turn90CCW()
R.turn90CCW()
R.turn90CCW()


B.setDelay(.005 / 8 * 1)
B.turn90CW()
B.turn90CW()
B.turn90CW()
B.turn90CCW()
B.turn90CCW()
B.turn90CCW()

U.setDelay(.005 / 8 * 1)
U.turn90CW()
U.turn90CW()
U.turn90CW()
U.turn90CCW()
U.turn90CCW()
U.turn90CCW()
