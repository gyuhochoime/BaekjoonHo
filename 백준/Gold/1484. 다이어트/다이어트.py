import sys
n = int(sys.stdin.readline())
lt = 1
rt = 2
arr = []
while rt <= 100000:
    dif = rt ** 2 - lt ** 2
    if dif == n:
        arr.append(rt)
        lt += 1
    elif dif < n:
        rt += 1
    else:
        lt += 1
if arr:
    for i in arr:
        print(i)
else:
    print(-1)