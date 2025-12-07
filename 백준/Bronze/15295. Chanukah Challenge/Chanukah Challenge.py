import sys
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    tot = 0
    for i in range(1, b + 1):
        tot += i
    tot += b
    print(a, tot)
