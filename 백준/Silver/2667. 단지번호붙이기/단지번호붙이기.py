import sys
from collections import deque
def BFS(si, sj):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1
    cnt = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                q.append((ni, nj))
                visited[ni][nj] = 1
                cnt += 1
    return cnt
n = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
ans = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visited[i][j] == 0:
            ans.append(BFS(i, j))
ans.sort()
print(len(ans), *ans, sep = "\n")
