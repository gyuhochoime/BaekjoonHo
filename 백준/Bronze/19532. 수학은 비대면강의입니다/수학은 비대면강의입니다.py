import sys
a, b, c, d, e, f = map(int, sys.stdin.readline().rstrip().split())
front_x, front_y, front_con = a, b, c
back_x, back_y, back_con = d, e, f
a, b, c = a * d, b * d, c * d
d, e, f = d * front_x, e * front_x, f * front_x
x = a - d
y = b - e
con = c - f
for i in range(-999, 1000):
    if i * y == con:
        y = i
        break
value_for_x = -(front_y * y) + front_con
for i in range(-999, 1000):
    if i * front_x == value_for_x:
        x = i
        break
if front_x == 0 and front_y == 0:
    print(back_x, back_y)
elif back_x == 0 and back_y == 0:
    print(front_x, front_y)
elif front_x == 0 and front_y != 0:
    print((back_con - back_y * front_con // front_y) // back_x, front_con // front_y)
elif back_x == 0 and back_y != 0:
    print((front_con - front_y * back_con // back_y) // front_x, back_con // back_y)
else:
    print(x, y)
