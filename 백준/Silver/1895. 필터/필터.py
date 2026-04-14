import sys
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
num = int(sys.stdin.readline())
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
cnt = 0
for i in range(1, n - 1):
    for j in range(1, m - 1):
        lst = []
        lst.append(arr[i][j])
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            lst.append(arr[ni][nj])
        lst.sort()
        if lst[4] >= num:
            cnt += 1
print(cnt)