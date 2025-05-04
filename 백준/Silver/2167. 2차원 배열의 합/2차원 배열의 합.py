import sys
input = sys.stdin.readline
a, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(a)]
prefix = [[0] * (b + 1) for _ in range(a + 1)]
for i in range(1, a + 1):
    for j in range(1, b + 1):
        prefix[i][j] = arr[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
T = int(input())
for _ in range(T):
    i, j, x, y = map(int, input().split())
    res = prefix[x][y] - prefix[i-1][y] - prefix[x][j-1] + prefix[i-1][j-1]
    print(res)
