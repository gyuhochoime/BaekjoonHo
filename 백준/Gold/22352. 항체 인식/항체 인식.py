import sys
from collections import deque
def bfs(si, sj):
    global flag_two
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1
    one = pre_arr[si][sj]
    fix = pos_arr[si][sj]
    while q:
        ci, cj = q.popleft()
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0:
                if pre_arr[ni][nj] == one:
                    if pos_arr[ni][nj] != fix:
                        flag_two = True
                        return
                    q.append((ni, nj))
                    visited[ni][nj] = 1
n, m = map(int, sys.stdin.readline().split())
pre_arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
pos_arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
flag_one = False
flag_two = False
for i in range(n):
    if flag_two:
        break
    for j in range(m):
        if flag_one and pre_arr[i][j] != pos_arr[i][j] and visited[i][j] == 0:
            flag_two = True
            break
        if pre_arr[i][j] != pos_arr[i][j] and visited[i][j] == 0:
            bfs(i, j)
            flag_one = True
if flag_two:
    print("NO")
else:
    print("YES")