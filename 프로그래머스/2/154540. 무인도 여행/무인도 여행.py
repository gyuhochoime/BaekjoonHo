from collections import deque
def solution(maps):
    def bfs(si, sj):
        q = deque()
        q.append((si, sj))
        visited[si][sj] = 0
        tmp = int(maps[si][sj])
        while q:
            ci, cj = q.popleft()
            for di, dj in dirs:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == -1 and maps[ni][nj] != "X":
                    q.append((ni, nj))
                    visited[ni][nj] = 0
                    tmp += int(maps[ni][nj])
        return tmp
    answer = []
    n = len(maps)
    m = len(maps[0])
    visited = [[-1] * m for _ in range(n)]
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in range(n):
        for j in range(m):
            if visited[i][j] == -1 and maps[i][j] != "X":
                answer.append(bfs(i, j))
    if answer:
        answer.sort()
        return answer
    else:
        return [-1]