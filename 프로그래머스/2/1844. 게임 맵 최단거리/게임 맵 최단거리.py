from collections import deque
def solution(maps):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque()
    q.append((0, 0))
    visited = [[-1] * len(maps[0]) for _ in range(len(maps))]
    visited[0][0] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < len(maps) and 0 <= nj < len(maps[0]) and maps[ni][nj] == 1 and visited[ni][nj] == -1:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1
    return visited[len(maps)-1][(len(maps[0])-1)]