import sys
n = int(sys.stdin.readline().rstrip())
tot = 1
for i in range(n, 0, -1):
    tot *= i
print(tot)
