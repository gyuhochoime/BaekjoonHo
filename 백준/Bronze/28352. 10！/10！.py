import sys
n = int(sys.stdin.readline().rstrip())
tot = 6
for i in range(11, n + 1):
    tot *= i
print(tot)
