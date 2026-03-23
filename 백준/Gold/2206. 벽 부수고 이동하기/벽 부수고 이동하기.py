import sys
from collections import deque
def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    while q:
        ci, cj, broke = q.popleft()
        if ci == n-1 and cj == m-1:
            return visited[ci][cj][broke]
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m:
                if arr[ni][nj] == 0 and visited[ni][nj][broke] == 0:
                    visited[ni][nj][broke] = visited[ci][cj][broke] + 1
                    q.append((ni, nj, broke))
                elif arr[ni][nj] == 1 and broke == 0:
                    visited[ni][nj][1] = visited[ci][cj][0] + 1
                    q.append((ni, nj, 1))
    return -1
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
print(bfs())