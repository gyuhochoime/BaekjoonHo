import sys
from collections import deque
def bfs(si, sj, fr):
    global flag
    sang_q = deque()
    sang_q.append((si, sj))
    visited[si][sj] = 1
    fire_q = deque()
    cnt = 0
    for fi, fj in fr:
        fire_q.append((fi, fj))
        visited[fi][fj] = -1
    while sang_q:
        for _ in range(len(fire_q)):
            ci, cj = fire_q.popleft()
            for di, dj in dirs:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < m and 0 <= nj < n and arr[ni][nj] != "#" and visited[ni][nj] != -1:
                    fire_q.append((ni, nj))
                    visited[ni][nj] = -1
        for _ in range(len(sang_q)):
            ci, cj = sang_q.popleft()
            for di, dj in dirs:
                ni, nj = ci + di, cj + dj
                if ni < 0 or ni >= m or nj < 0 or nj >= n:
                    flag = True
                    cnt += 1
                    return cnt
                if 0 <= ni < m and 0 <= nj < n and arr[ni][nj] == "." and visited[ni][nj] == 0:
                    sang_q.append((ni, nj))
                    visited[ni][nj] = 1
        cnt += 1
T = int(sys.stdin.readline())
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    arr = [list(sys.stdin.readline().rstrip()) for _ in range(m)]
    visited = [[0] * n for _ in range(m)]
    fire = []
    flag = False
    ans = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == "*":
                fire.append((i, j))
    for i in range(m):
        for j in range(n):
            if arr[i][j] == "@":
                ans = bfs(i, j, fire)
    if flag:
        print(ans)
    else:
        print("IMPOSSIBLE")
