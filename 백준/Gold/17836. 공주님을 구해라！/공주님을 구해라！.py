import sys
from collections import deque
def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 0
    while q:
        ci, cj, gram = q.popleft()
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj][gram] == -1:
                if arr[ni][nj] == 2:
                    q.append((ni, nj, 0))
                    q.append((ni, nj, 1))
                    visited[ni][nj][gram] = visited[ci][cj][gram] + 1
                    visited[ni][nj][1] = visited[ci][cj][gram] + 1
                if gram == 1:
                    q.append((ni, nj, gram))
                    visited[ni][nj][gram] = visited[ci][cj][gram] + 1
                elif gram == 0 and arr[ni][nj] == 0:
                    q.append((ni, nj, gram))
                    visited[ni][nj][gram] = visited[ci][cj][gram] + 1
    if visited[n-1][m-1][0] == -1 and visited[n-1][m-1][1] == -1:
        return "Fail"
    elif visited[n-1][m-1][0] == -1 and visited[n-1][m-1][1] != -1:
        return visited[n-1][m-1][1]
    elif visited[n-1][m-1][0] != -1 and visited[n-1][m-1][1] != -1:
        return min(visited[n-1][m-1][0], visited[n-1][m-1][1])
n, m, k = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[[-1] * 2 for _ in range(m)] for _ in range(n)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
ans = bfs()
if ans == "Fail":
    print(ans)
else:
    if ans <= k:
        print(ans)
    else:
        print("Fail")