import sys
n = int(sys.stdin.readline().rstrip())
arr = list(sys.stdin.readline().rstrip())
tot = 0
for i in range(n):
    tot += ord(arr[i])-64
print(tot)
