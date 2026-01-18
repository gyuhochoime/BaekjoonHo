import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
tmp = []
for _ in range(n):
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    tmp.append(a)
for i in range(n):
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(m):
        result = tmp[i][j] + a[j]
        print(result, end = " ")
    print()
