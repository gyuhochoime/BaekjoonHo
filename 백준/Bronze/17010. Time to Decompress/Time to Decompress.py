import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    n, m = map(str, sys.stdin.readline().rstrip().split())
    print(m * int(n))
