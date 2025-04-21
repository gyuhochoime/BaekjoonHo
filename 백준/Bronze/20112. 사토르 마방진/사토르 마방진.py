import sys
T = int(sys.stdin.readline().rstrip())
arr = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(T)]
cnt = 0
for i in range(T):
    for j in range(T):
        if arr[i][j] == arr[j][i]:
            cnt += 1
if cnt == T ** 2:
    print("YES")
else:
    print("NO")
