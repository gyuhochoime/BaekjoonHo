import sys
def Count(leng):
    cnt = 0
    for x in line:
        cnt += (x // leng)
    return cnt
n, m = map(int, sys.stdin.readline().rstrip().split())
line = []
res = 0
for _ in range(n):
    a = int(sys.stdin.readline().rstrip())
    line.append(a)
line.sort()
lt = 1
rt = line[-1]
while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= m:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)
