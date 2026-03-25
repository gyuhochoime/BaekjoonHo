import sys
from collections import deque
def bfs(si, sj, lst):
    hedge_q = deque()
    hedge_q.append((si, sj))
    water_q = deque()
    for ci, cj in lst:
        water_q.append((ci, cj))
        visited[ci][cj] = -9
    visited[si][sj] = 0
    while hedge_q:
        for _ in range(len(hedge_q)):
            ci, cj = hedge_q.popleft()
            for di, dj in dirs:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == "D" and visited[ci][cj] != -9:
                    return visited[ci][cj] + 1
                if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == "." and visited[ni][nj] == -1:
                    hedge_q.append((ni, nj))
                    visited[ni][nj] = visited[ci][cj] + 1
        for _ in range(len(water_q)):
            ci, cj = water_q.popleft()
            for di, dj in dirs:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] != "D" and arr[ni][nj] != "X" and visited[ni][nj] != -9:
                    water_q.append((ni, nj))
                    visited[ni][nj] = -9
    return "KAKTUS"
n, m = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
water = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == "*":
            water.append((i, j))
for i in range(n):
    for j in range(m):
        if arr[i][j] == "S":
            print(bfs(i, j, water))
            break
