import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arm = []
money = int(sys.stdin.readline().rstrip())
tot = money
arr.sort()
for i in range(n):
    if tot // (n - i) >= arr[i]:
        tot -= arr[i]
    else:
        arm.append(tot // (n - i))
        break
if len(arm) > 0:
    print(min(arm))
else:
    print(arr[n-1])
