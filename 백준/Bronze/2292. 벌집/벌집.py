import sys
n = int(sys.stdin.readline().rstrip())
cnt = 1
k = 1
m = n
while n > 0:
    if cnt == 1:
        n = n - k - 6 * cnt
        cnt += 1
        continue
    else:
        n = n - 6 * cnt
        cnt += 1
if m == 1:
    print(1)
else:
    print(cnt)
