import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
tot = 0
tot += arr.pop()
tot += sum(arr) / 2
print(tot)
