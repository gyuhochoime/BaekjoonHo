import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
tot = sum(arr)
tos = 0
for i in arr:
    tot -= i
    tos += tot * i
print(tos)
