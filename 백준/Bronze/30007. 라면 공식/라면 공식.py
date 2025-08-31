import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    n, m, k = map(int, sys.stdin.readline().rstrip().split())
    print(m + n * (k - 1))
