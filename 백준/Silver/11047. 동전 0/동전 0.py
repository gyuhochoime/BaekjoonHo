import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
tot = 0
for i in range(n):
    k = int(sys.stdin.readline().rstrip())
    arr.append(k)
arr.sort(reverse = True)
for i in arr:
    if m >= i:
        tot += m // i
        m -= i * (m // i)
print(tot)
