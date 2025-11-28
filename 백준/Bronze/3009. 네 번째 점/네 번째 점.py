import sys
arn = dict()
arm = dict()
for _ in range(3):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    if n in arn:
        arn[n] = 0
    else:
        arn[n] = 1
    if m in arm:
        arm[m] = 0
    else:
        arm[m] = 1
xn = [(key, value) for key, value in arn.items()]
ym = [(key, value) for key, value in arm.items()]
xn.sort(key = lambda x: (-x[1]))
ym.sort(key = lambda x: (-x[1]))
print(xn[0][0], ym[0][0])
