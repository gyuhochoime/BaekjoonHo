import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
cnt = 0
arr.sort()
lt, rt = 0, n - 1
while lt < rt:
    tmp = arr[lt] + arr[rt]
    if tmp == m:
        cnt += 1
        lt += 1
    elif tmp < m:
        lt += 1
    else:
        rt -= 1
print(cnt)
