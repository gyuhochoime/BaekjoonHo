import sys

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    v, e = map(int, sys.stdin.readline().rstrip().split())
    mun = e - v + 2
    print(mun)
