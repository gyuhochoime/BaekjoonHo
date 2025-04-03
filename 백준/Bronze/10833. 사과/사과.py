import sys
T = int(sys.stdin.readline().rstrip())
tot = 0
for i in range(T):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    tot += m % n
print(tot)
