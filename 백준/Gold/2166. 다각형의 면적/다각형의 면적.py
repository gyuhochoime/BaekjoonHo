import sys
n = int(sys.stdin.readline())
spot = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    spot.append((a, b))
spot.append(spot[0])
tot = 0
for i in range(n):
    tot += spot[i][0] * spot[i+1][1] - spot[i+1][0] * spot[i][1]
print(abs(tot) / 2)
