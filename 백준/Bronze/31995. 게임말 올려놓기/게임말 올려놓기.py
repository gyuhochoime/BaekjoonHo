import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
if n > 1 and m > 1:
    print((n - 1) * (m - 1) * 2)
else:
    print(0)
