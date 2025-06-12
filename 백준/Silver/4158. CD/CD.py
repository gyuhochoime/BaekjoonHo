import sys
while True:
    n, m = map(int, sys.stdin.readline().rstrip().split())
    if n == 0 and m == 0:
        break
    arn = set()
    arm = set()
    cnt = 0
    for i in range(n):
        an = int(sys.stdin.readline().rstrip())
        arn.add(an)
    for i in range(m):
        am = int(sys.stdin.readline().rstrip())
        arm.add(am)
    for i in arn:
        if i in arm:
            cnt += 1
    print(cnt)

