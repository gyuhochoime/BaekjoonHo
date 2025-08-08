import sys
arn = list(map(int, sys.stdin.readline().rstrip().split()))
arm = list(map(int, sys.stdin.readline().rstrip().split()))
tot = 0
for i in range(3):
    if arm[i] - arn[i] >= 0:
        tot += arm[i] - arn[i]
print(tot)
