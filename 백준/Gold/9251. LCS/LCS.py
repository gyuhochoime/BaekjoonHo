import sys
a = list(sys.stdin.readline().rstrip())
b = list(sys.stdin.readline().rstrip())
n = len(a)
m = len(b)
arr = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i-1] == b[j-1]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i][j-1], arr[i-1][j])
print(arr[n][m])