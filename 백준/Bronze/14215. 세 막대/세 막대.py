import sys
n = list(map(int, sys.stdin.readline().rstrip().split()))
n.sort()
m = n[0] + n[1] - 1
if m > n[2]:
    print(sum(n))
else:
    print(n[0] + n[1] + m)
