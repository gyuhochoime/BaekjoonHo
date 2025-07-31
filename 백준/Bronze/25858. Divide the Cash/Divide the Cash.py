import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
tot = 0
for i in range(n):
    t = int(sys.stdin.readline().rstrip())
    tot += t
    arr.append(t)
for i in arr:
    print((m // tot) * i)
