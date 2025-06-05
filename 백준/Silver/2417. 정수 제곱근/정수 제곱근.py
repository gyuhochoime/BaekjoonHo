import sys
n = int(sys.stdin.readline().rstrip())
lt = 1
rt = n
ans = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if mid ** 2 >= n:
        ans = mid
        rt = mid - 1
    elif mid ** 2 < n:
        lt = mid + 1
print(ans)

