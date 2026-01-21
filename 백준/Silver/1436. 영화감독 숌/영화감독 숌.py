import sys
n = int(sys.stdin.readline().rstrip())
cnt = 0
arr = [0] * 3000001
for i in range(3000001):
    if "666" in str(i):
        arr[i] = 1
for i in range(3000001):
    if arr[i] == 1:
        cnt += 1
    if cnt == n:
        print(i)
        break
