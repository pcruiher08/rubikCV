from motor import Motor


F = Motor(26,19)
R = Motor(13,6)
B = Motor(21, 20)

F.setDelay(.005 / 8 * 2)
F.turn90CW()
F.turn90CW()
F.turn90CW()
F.turn90CCW()
F.turn90CCW()
F.turn90CCW()


R.setDelay(.005 / 8 * 2)
R.turn90CW()
R.turn90CW()
R.turn90CW()
R.turn90CCW()
R.turn90CCW()
R.turn90CCW()


B.setDelay(.005 / 8 * 2)
B.turn90CW()
B.turn90CW()
B.turn90CW()
B.turn90CCW()
B.turn90CCW()
B.turn90CCW()
