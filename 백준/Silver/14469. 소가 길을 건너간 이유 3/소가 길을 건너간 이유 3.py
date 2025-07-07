import sys
T = int(sys.stdin.readline().rstrip())
lt = []
for i in range(T):
    at, ct = map(int, sys.stdin.readline().rstrip().split())
    lt.append((at, ct))
lt.sort(key = lambda x: (x[0], x[1]))
et = 0
for at, ct in lt:
    if et <= at:
        et = at + ct
    else:
        et += ct
print(et)
