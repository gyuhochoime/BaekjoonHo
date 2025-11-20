import sys
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    com = 0
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if b % 4 == 0:
        com = 4
    else:
        com = b % 4
    tot = str(a ** com)
    if tot[-1] == "0":
        print(10)
    else:
        print(tot[-1])
