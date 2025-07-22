import sys
n, m, k = map(int, sys.stdin.readline().rstrip().split())
arn = list(map(int, sys.stdin.readline().rstrip().split()))
arm = list(map(int, sys.stdin.readline().rstrip().split()))
ark = list(map(int, sys.stdin.readline().rstrip().split()))
arn.sort(reverse = True)
arm.sort(reverse = True)
ark.sort(reverse = True)
s = min(n, m, k)
tot = sum(arn) + sum(arm) + sum(ark)
hal = 0
for i in range(s):
    hal += (arn[i] + arm[i] + ark[i]) // 10 * 9
for i in range(n - s):
    hal += arn[s+i]
for i in range(m - s):
    hal += arm[s+i]
for i in range(k - s):
    hal += ark[s+i]
print(tot)
print(hal)
