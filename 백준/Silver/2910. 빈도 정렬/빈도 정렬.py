import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
a = dict()
been = []
for i in arr:
    if i not in a:
        a[i] = 1
    else:
        a[i] += 1
for key, val in a.items():
    been.append((key, val))
been.sort(key = lambda x: (-x[1]))
for key, val in been:
    for _ in range(val):
        print(str(key), end = " ")
