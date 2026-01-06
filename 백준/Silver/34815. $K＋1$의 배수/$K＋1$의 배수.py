import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
a = [x for x in range(1, n + 1)]
so = sum(a[:k])
de = sum(a[n-k:])
for i in range(so, de + 1):
    if i % (k + 1) == 0:
        print("YES")
        break
else:
    print("NO")
