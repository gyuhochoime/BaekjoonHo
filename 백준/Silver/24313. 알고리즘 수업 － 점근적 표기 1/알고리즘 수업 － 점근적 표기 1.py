import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
c = int(sys.stdin.readline().rstrip())
d = int(sys.stdin.readline().rstrip())
if n > c:
    print(0)
else:
    if n * d + m <= c * d:
        print(1)
    else:
        print(0)
