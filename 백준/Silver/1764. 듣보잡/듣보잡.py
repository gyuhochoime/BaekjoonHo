import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arn = set()
arm = set()
arnm = []
for i in range(n):
    a = sys.stdin.readline().rstrip()
    arn.add(a)
for i in range(m):
    b = sys.stdin.readline().rstrip()
    arm.add(b)
for i in arn:
    if i in arm:
        arnm.append(i)
arnm.sort()
print(len(arnm))
for i in arnm:
    print(i)
