import sys
n = int(sys.stdin.readline().rstrip())
tot = 5
for i in range(2, n + 1):
    tot += 4 + 3 * (i - 1)
print(tot % 45678)
