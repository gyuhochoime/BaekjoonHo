import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
tot = 0
for i in arr:
    if i % 2 == 1:
        tot += i // 2 + 1
    else:
        tot += i // 2
print(tot)
