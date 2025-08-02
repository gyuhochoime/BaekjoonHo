import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    a = m * 2 - n
    print(a, m - a)
