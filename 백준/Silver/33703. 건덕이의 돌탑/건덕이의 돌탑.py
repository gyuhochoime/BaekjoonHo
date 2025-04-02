import sys
n = int(sys.stdin.readline().rstrip())
tot = 0
for i in range(1, n + 1):
    tot += i
print(tot)
