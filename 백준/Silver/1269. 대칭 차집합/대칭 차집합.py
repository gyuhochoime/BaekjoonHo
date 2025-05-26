import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arn = list(map(int, sys.stdin.readline().rstrip().split()))
arm = list(map(int, sys.stdin.readline().rstrip().split()))
arr = []
for i in arn:
    arr.append(i)
for i in arm:
    arr.append(i)
k = len(arr)
arr = set(arr)
arr = list(arr)
s = len(arr)
cha = k - s
print(len(arn) - cha + len(arm) - cha)
