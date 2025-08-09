import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
if n >= 12 and n <= 16 and m == 0:
    print(320)
else:
    print(280)
