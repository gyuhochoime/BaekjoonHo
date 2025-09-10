import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
mile = m
arr = []
cnt = 0
for _ in range(n):
    p, l = map(int, sys.stdin.readline().rstrip().split())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    a.sort(reverse = True)
    if p < l:
        arr.append(1)
    else:
        arr.append(a[l-1])
arr.sort()
for i in arr:
    mile -= i
    if mile < 0:
        break
    else:
        cnt += 1
print(cnt)
