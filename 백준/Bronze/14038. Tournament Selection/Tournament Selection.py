import sys
tot = 0
for _ in range(6):
    n = sys.stdin.readline().rstrip()
    if n == "W":
        tot += 1
if tot == 5 or tot == 6:
    print(1)
elif tot == 3 or tot == 4:
    print(2)
elif tot == 1 or tot == 2:
    print(3)
else:
    print(-1)
