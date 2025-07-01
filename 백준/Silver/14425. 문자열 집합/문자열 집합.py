import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arn = []
arm = []
cnt = 0
for i in range(n):
    a = sys.stdin.readline().rstrip()
    arn.append(a)
for j in range(m):
    b = sys.stdin.readline().rstrip()
    arm.append(b)
for i in arm:
    if i in arn:
        cnt += 1
print(cnt)
