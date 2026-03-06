import sys
from collections import deque
def bfs(s):
    q = deque()
    q.append(s)
    visited = [-1] * 100001
    visited[s] = 0
    while q:
        a = q.popleft()
        if a == m:
            return visited[a]
        for i in [a + 1, a - 1, 2 * a]:
            if 0 <= i < 100001 and visited[i] == -1:
                q.append(i)
                visited[i] = visited[a] + 1
n, m = map(int, sys.stdin.readline().split())
ans = bfs(n)
print(ans)
