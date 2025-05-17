import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
tot = 0
cnt = 0
for i in range(len(arr)):
    cnt += arr[i]
    tot += cnt
print(tot)
