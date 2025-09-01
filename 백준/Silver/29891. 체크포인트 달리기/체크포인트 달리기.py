import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arn = []
arm = []
for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    if a >= 0:
        arn.append(a)
    else:
        arm.append(a)
arn.sort()
arm.sort(reverse = True)
k = len(arn) - 1
r = len(arm) - 1
tot = 0
while k >= 0:
    tot += arn[k] * 2
    k -= m
while r >= 0:
    tot -= arm[r] * 2
    r -= m
print(tot)
