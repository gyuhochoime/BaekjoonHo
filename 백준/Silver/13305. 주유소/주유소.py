import sys
n = int(sys.stdin.readline())
dis = list(map(int, sys.stdin.readline().split()))
oil = list(map(int, sys.stdin.readline().split()))
tot = 0
min_oil = 1000000001
for i in range(n - 1):
    min_oil = min(min_oil, oil[i])
    tot += min_oil * dis[i]
print(tot)
