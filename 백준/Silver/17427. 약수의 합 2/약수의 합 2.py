import sys
n = int(sys.stdin.readline())
tot = 0
for i in range(1, n + 1):
    tot += (n // i) * i
print(tot)