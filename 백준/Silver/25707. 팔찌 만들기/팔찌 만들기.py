import sys
T = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
tot = 0
for i in range(T):
    tot += abs(arr[i] - arr[i-1])
print(tot)
