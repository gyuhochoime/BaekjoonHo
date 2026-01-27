import sys
def DFS(c):
    global cnt
    cnt += 1
    visited[c] = 1
    for i in adj[c]:
        if not visited[i]:
            DFS(i)
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    adj[s].append(e)
    adj[e].append(s)
cnt = 0
visited = [0] * (n + 1)
DFS(1)
print(cnt - 1)
