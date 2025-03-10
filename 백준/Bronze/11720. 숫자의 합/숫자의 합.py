import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip()))
m = 0
for i in range(n):
    m += arr[i]
print(m)

