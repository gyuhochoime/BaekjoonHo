import sys
n = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))
cnt = 0
for i in range(n):
    a = arr[i]
    tmp = arr[:i] + arr[i+1:]
    lt = 0
    rt = len(tmp) - 1
    while lt < rt:
        mid = tmp[lt] + tmp[rt]
        if mid == a:
            cnt += 1
            break
        elif mid < a:
            lt += 1
        elif mid > a:
            rt -= 1
print(cnt)
