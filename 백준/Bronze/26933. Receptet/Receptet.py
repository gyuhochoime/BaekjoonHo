import sys
T = int(sys.stdin.readline().rstrip())
tot = 0
for i in range(T):
    n, m, k = map(int, sys.stdin.readline().rstrip().split())
    if m > n:
        tot += (m - n) * k
print(tot)
