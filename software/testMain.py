from motor import Motor


D = Motor(20,21)
D.setDelay(.005 / 8 * 4)

D.turn90CW()
D.turn90CW()
D.turn90CW()
D.turn90CCW()
D.turn90CCW()
D.turn90CCW()
