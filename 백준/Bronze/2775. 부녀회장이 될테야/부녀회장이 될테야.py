import sys
arr = [[0] * 14 for _ in range(15)]
for i in range(14):
    arr[0][i] = i + 1
for i in range(1, 15):
    for j in range(14):
        if j == 0:
            arr[i][j] = arr[i-1][j]
        else:
            arr[i][j] = arr[i-1][j] + arr[i][j-1]
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    a = int(sys.stdin.readline().rstrip())
    b = int(sys.stdin.readline().rstrip())
    print(arr[a][b-1])
