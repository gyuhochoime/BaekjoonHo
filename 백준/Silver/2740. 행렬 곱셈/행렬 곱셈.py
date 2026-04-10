import sys
n, m = map(int, sys.stdin.readline().split())
arr_1 = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
k, r = map(int, sys.stdin.readline().split())
arr_2 = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
arr_gop = [[0] * r for _ in range(n)]
for i in range(n):
    for j in range(r):
        for s in range(m):
            arr_gop[i][j] += arr_1[i][s] * arr_2[s][j]
for i in arr_gop:
    print(*i)