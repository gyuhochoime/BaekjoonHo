import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
cnt = 0
while arr:
    if arr[0] + arr[len(arr)-1] <= m and len(arr) >= 2:
        arr.pop()
        arr.pop(0)
        cnt += 1
    else:
        arr.pop()
print(cnt)
