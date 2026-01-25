import sys 
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
lt = 1
rt = arr[-1]
while lt <= rt:
    tot = 0
    mid = (lt + rt) // 2
    for x in arr:
        if x > mid:
            tot += x - mid
    if tot < m:
        rt = mid - 1
    else:
        lt = mid + 1
print(rt)
