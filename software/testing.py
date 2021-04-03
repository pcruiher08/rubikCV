from rubik_solver import utils

cube = "wowg y bwyo gygy b yogg rowb r gywr borw g gybr bwor o rbwb orgo w ryby"

print(utils.solve(cube, 'Kociemba'))
utils.pprint(cube)
res = ""
for i in cube:
    if i == 'w':
        res += 'D'
    if i == 'o':
        res += 'B'
    if i == 'g':
        res += 'R'
    if i == 'r':
        res += 'F'
    if i == 'b':
        res += 'L'
    if i == 'y':
        res += 'U'

print(res)