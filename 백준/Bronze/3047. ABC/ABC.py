import sys
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
arn = dict()
arn["A"] = arr[0]
arn["B"] = arr[1]
arn["C"] = arr[2]
order = list((sys.stdin.readline().rstrip()))
for i in order:
    print(arn[i], end = " ")
