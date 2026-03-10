import sys
from collections import deque
def bfs(si, sj):
    global flag
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1
    popul = deque()
    popul.append((si, sj))
    tot = arr[si][sj]
    num = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < n and m <= abs(arr[ci][cj] - arr[ni][nj]) <= k and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
                popul.append((ni, nj))
                tot += arr[ni][nj]
                num += 1
    if num >= 2:
        a = int(tot / num)
        flag = True
        while popul:
            pi, pj = popul.popleft()
            arr[pi][pj] = a
n, m, k = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cnt = 0
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while True:
    visited = [[0] * n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                bfs(i, j)
    if flag == False:
        break
    cnt += 1
print(cnt)
