import sys
a, b, c = map(int, sys.stdin.readline().rstrip().split())
suik = c - b
if b >= c:
    print(-1)
else:
    sonik = a // suik + 1
    print(sonik)
