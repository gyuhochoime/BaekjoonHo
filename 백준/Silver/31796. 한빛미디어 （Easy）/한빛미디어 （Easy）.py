import sys
T = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
cnt = 1
arr.sort()
tmp = arr[0]
for i in range(T):
    if arr[i] >= tmp * 2:
        cnt += 1
        tmp = arr[i]
print(cnt)
