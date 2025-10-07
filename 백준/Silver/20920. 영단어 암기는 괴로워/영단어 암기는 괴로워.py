import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = dict()
alpha = []
for _ in range(n):
    a = sys.stdin.readline().rstrip()
    if len(a) >= m:
        if a in arr:
            arr[a] += 1
        else:
            arr[a] = 1
for key, val in arr.items():
    alpha.append((key, val))
alpha.sort(key = lambda x: (-x[1], -len(x[0]), x[0]))
for key, val in alpha:
    print(key)
