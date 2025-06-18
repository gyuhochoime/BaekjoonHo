import sys
n, m, k = map(int, sys.stdin.readline().rstrip().split())
r = int(sys.stdin.readline().rstrip())
tot = (n * 3600 + m * 60 + k + r) % 86400
hour = tot // 3600
minute = tot % 3600 // 60
second = tot % 3600 % 60
print(hour, minute, second)
