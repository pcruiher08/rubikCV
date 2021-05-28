from motor import Motor


R = Motor(26,19)
B = Motor(13,6)
'''
L = Motor(12,16)

R.setDelay(.005 / 8 * 4)
L.setDelay(.005 / 8 * 4)


R.turn90CW()
L.turn90CW()

R.turn90CW()
L.turn90CW()

R.turn90CW()
L.turn90CW()

R.turn90CCW()
L.turn90CCW()

R.turn90CCW()
L.turn90CCW()

R.turn90CCW()
L.turn90CCW()
'''


R.setDelay(.005 / 8 * 4)
R.turn90CW()
R.turn90CW()
R.turn90CW()
R.turn90CCW()
R.turn90CCW()
R.turn90CCW()


B.setDelay(.005 / 8 * 4)
B.turn90CW()
B.turn90CW()
B.turn90CW()
B.turn90CCW()
B.turn90CCW()
B.turn90CCW()
