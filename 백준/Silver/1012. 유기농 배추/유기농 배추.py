import sys
sys.setrecursionlimit(10 ** 6)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def DFS(y, x):
    global visited
    visited[y][x] = 1
    for i in range(4):
        newY = y + dy[i]
        newX = x + dx[i]
        if graph[newY][newX] == 1 and visited[newY][newX] == 0:
            DFS(newY, newX)
T = int(sys.stdin.readline())
MAX = 60
for _ in range(T):
    n, m, k = map(int, sys.stdin.readline().split())
    graph = [[0] * (MAX) for _ in range(MAX)]
    visited = [[0] * (MAX) for _ in range(MAX)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[y+1][x+1] = 1
    answer = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if graph[i][j] == 1 and visited[i][j] == 0:
                DFS(i, j)
                answer += 1
    print(answer)
