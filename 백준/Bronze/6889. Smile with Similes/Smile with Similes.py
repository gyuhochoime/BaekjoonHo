import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
arn = []
arm = []
for i in range(n):
    a = sys.stdin.readline().rstrip()
    arn.append(a)
for i in range(m):
    b = sys.stdin.readline().rstrip()
    arm.append(b)
for i in arn:
    for j in arm:
        print(i + " as " + j)
