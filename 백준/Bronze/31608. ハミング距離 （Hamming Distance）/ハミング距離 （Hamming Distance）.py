import sys
n = int(sys.stdin.readline().rstrip())
arn = list(map(str, sys.stdin.readline().rstrip()))
arm = list(map(str, sys.stdin.readline().rstrip()))
cnt = 0
for i in range(n):
    if arn[i] != arm[i]:
        cnt += 1
print(cnt)
