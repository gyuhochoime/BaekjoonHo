import sys
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
b = list(map(int, sys.stdin.readline().rstrip().split()))
tot = 0
a.sort()
b.sort(reverse = True)
for i in range(n):
    tot += a[i] * b[i]
print(tot)
