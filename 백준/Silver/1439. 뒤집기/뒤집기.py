import sys
arr = list(map(str, sys.stdin.readline().rstrip()))
cnt = 0
for i in range(len(arr) - 1):
    tmp = arr[i]
    if arr[i] != arr[i+1]:
        cnt += 1
if cnt % 2 == 0:
    print(cnt // 2)
else:
    print(cnt // 2 + 1)
