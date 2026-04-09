import sys
from collections import deque
def bfs():
    q = deque()
    for i, j in bomb:
        q.append((i, j))
        visited[i][j] = "."
    for ci, cj in q:
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m:
                visited[ni][nj] = "."
n, m, k = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
num = k % 4
if k == 1:
    for i in arr:
        for j in i:
            print(j, end = "")
        print()
elif num == 0 or num == 2:
    lst = [["O"] * m for _ in range(n)]
    for i in lst:
        for j in i:
            print(j, end = "")
        print()
else:
    visited = [["O"] * m for _ in range(n)]
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    bomb = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == "O":
                bomb.append((i, j))
    bfs()
    first = visited
    if num == 3:
        for i in first:
            for j in i:
                print(j, end = "")
            print()
    else:
        visited = [["O"] * m for _ in range(n)]
        bomb = []
        for i in range(n):
            for j in range(m):
                if first[i][j] == "O":
                    bomb.append((i, j))
        bfs()
        for i in visited:
            for j in i:
                print(j, end = "")
            print()