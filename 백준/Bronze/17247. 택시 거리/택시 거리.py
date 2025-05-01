import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
cnt = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            cnt.append([i, j])
distance = (abs(cnt[1][0] - cnt[0][0]) + abs(cnt[1][1] - cnt[0][1]))
print(distance)
