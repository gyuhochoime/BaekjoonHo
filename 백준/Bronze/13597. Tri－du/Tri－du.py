import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
if n != m:
    print(max(n, m))
else:
    print(n)
