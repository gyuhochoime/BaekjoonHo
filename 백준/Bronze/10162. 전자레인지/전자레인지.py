import sys
n = int(sys.stdin.readline())
if n % 10 != 0:
    print(-1)
else:
    fm = om = ts = 0
    fm = n // 300
    n %= 300
    om = n // 60
    n %= 60
    ts = n // 10
    print(fm, om, ts)
