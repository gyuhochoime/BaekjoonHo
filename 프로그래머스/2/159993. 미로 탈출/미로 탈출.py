from collections import deque
def solution(maps):
    def bfs(si, sj):
        q = deque()
        q.append((si, sj))
        visited[si][sj] = 0
        lever_flag = False
        tmp = 0
        while q:
            if lever_flag:
                break
            ci, cj = q.popleft()
            for di, dj in dirs:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == -1:
                    if maps[ni][nj] != "X" and maps[ni][nj] != "L":
                        visited[ni][nj] = visited[ci][cj] + 1
                        q.append((ni, nj))
                    elif maps[ni][nj] == "L":
                        tmp += visited[ci][cj] + 1
                        q = deque()
                        q.append((ni, nj))
                        new_visited[ni][nj] = 0
                        lever_flag = True
                        break
        while q:
            ci, cj = q.popleft()
            for di, dj in dirs:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < n and 0 <= nj < m and new_visited[ni][nj] == -1:
                    if maps[ni][nj] != "X" and maps[ni][nj] != "E":
                        new_visited[ni][nj] = new_visited[ci][cj] + 1
                        q.append((ni, nj))
                    elif maps[ni][nj] == "E":
                        tmp += new_visited[ci][cj] + 1
                        return tmp
        return -1
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[-1] * m for _ in range(n)]
    new_visited = [[-1] * m for _ in range(n)]
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                answer = bfs(i, j)
                break
    return answer