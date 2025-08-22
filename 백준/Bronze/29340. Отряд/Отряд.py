import sys
arn = list(map(int, sys.stdin.readline().rstrip()))
arm = list(map(int, sys.stdin.readline().rstrip()))
arr = []
for i in range(len(arm)):
    arr.append(max(arn[i], arm[i]))
for i in arr:
    print(i, end = "")
