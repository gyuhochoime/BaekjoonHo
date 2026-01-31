import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
arr = deque()
arr.append(n)
visited = [-1] * 100001
visited[n] = 0
while arr:
    a = arr.popleft()
    if a == m:
        print(visited[a])
        break
    for i in [a - 1, a + 1, a * 2]:
        if i >= 0 and i <= 100000 and visited[i] == -1:
            visited[i] = visited[a] + 1
            arr.append(i)
