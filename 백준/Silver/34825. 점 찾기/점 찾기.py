import sys
xa, ya = map(int, sys.stdin.readline().rstrip().split())
xb, yb = map(int, sys.stdin.readline().rstrip().split())

imp = abs(xb - xa) + abs(yb - ya)

if imp % 2 != 0:
    print(-1)
    exit()

dis = imp // 2
x, y = xa, ya
dx = xb - xa
dy = yb - ya

move = min(abs(dx), dis)
x += move if dx > 0 else -move
dis -= move

y += dis if dy > 0 else -dis

print(x, y)
