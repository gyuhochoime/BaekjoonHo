import sys
n = int(sys.stdin.readline().rstrip())
arn = list(map(int, sys.stdin.readline().rstrip().split()))
arm = list(map(int, sys.stdin.readline().rstrip().split()))
cnt = 0
for i in range(n):
    if arm[i] >= arn[i]:
        cnt += 1
print(cnt)
