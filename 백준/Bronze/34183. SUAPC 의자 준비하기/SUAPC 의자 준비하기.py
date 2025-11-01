import sys
n, m, k, r = map(int, sys.stdin.readline().rstrip().split())
if n * 3 <= m:
    print(0)
else:
    print((n * 3 - m) * k + r)
    
