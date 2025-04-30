import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
tot = sum(arr) + (n - 1) * 8
day = tot // 24
hour = tot % 24
print(day, hour)
