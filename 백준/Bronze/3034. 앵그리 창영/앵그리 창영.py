import sys
n, m, k = map(int, sys.stdin.readline().rstrip().split())
tot = m ** 2 + k ** 2
for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    if a ** 2 <= tot:
        print("DA")
    else:
        print("NE")
