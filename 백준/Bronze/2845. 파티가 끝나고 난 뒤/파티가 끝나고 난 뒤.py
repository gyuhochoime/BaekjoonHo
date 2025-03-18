import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
k = list(map(int, sys.stdin.readline().rstrip().split()))
out = []
par = n * m
for i in k:
    out.append(i - par)
for i in range(len(out)):
    print(out[i], end = " ")
