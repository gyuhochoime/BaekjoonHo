import sys
n = int(sys.stdin.readline().rstrip())
arr = dict()
arn = list(map(str, sys.stdin.readline().rstrip().split()))
arm = list(map(str, sys.stdin.readline().rstrip().split()))
for i in arn:
    if i not in arr:
        arr[i] = 1
for i in arm:
    if i in arr:
        arr[i] = 0
ing = [(key, value) for key, value in arr.items()]
ing.sort(key = lambda x: (x[1]))
print(ing[n-1][0])
