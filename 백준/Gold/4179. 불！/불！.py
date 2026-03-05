import sys
from collections import deque
def bfs(jsi, jsj, fs):
    global flag
    jihoon_q = deque()
    jihoon_q.append((jsi, jsj))
    visited[jsi][jsj] = 1
    fire_q = deque()
    for fsi, fsj in fs:
        fire_q.append((fsi, fsj))
        visited[fsi][fsj] = -1
    cnt = 0
    while jihoon_q:
        for _ in range(len(jihoon_q)):
            ci, cj = jihoon_q.popleft()
            if visited[ci][cj] == 1:
                for di, dj in dirs:
                    ni, nj = ci + di, cj + dj
                    if ni == -1 or ni == n or nj == -1 or nj == m:
                        flag = True
                        cnt += 1
                        break
                    if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == "." and visited[ni][nj] == 0:
                        jihoon_q.append((ni, nj))
                        visited[ni][nj] = 1
            elif visited[ci][cj] == -1:
                continue
            if flag:
                break
        if flag:
            break
        for _ in range(len(fire_q)):
            ci, cj = fire_q.popleft()
            for di, dj in dirs:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] != "#" and visited[ni][nj] != -1:
                    fire_q.append((ni, nj))
                    visited[ni][nj] = -1
        cnt += 1
    return cnt
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
jihoon = []
fire = []
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
flag = False
for i in range(n):
    for j in range(m):
        if arr[i][j] == "J":
            jihoon.append((i, j))
        elif arr[i][j] == "F":
            fire.append((i, j))
ans = bfs(jihoon[0][0], jihoon[0][1], fire)
if flag:
    print(ans)
else:
    print("IMPOSSIBLE")