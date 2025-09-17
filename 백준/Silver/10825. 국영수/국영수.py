import sys
T = int(sys.stdin.readline().rstrip())
arr = []
for i in range(T):
    n, m, k, r = map(str, sys.stdin.readline().rstrip().split())
    arr.append((n, int(m), int(k), int(r)))
arr.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))
for a, b, c, d in arr:
    print(a)
