import sys
while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    tot = 0
    for i in arr:
        if tot + i <= 300:
            tot += i
    print(tot)
