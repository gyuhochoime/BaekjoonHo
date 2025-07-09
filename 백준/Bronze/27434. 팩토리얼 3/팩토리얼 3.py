import sys
T = int(sys.stdin.readline().rstrip())
tot = 1
for i in range(1, T + 1):
    tot *= i
if T == 0:
    print(1)
else:
    print(tot)
