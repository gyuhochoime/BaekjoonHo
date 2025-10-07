import sys
n = int(sys.stdin.readline().rstrip())
arr = dict()
most = []
for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    if a in arr:
        arr[a] += 1
    else:
        arr[a] = 1
for key, val in arr.items():
    most.append((key, val))
most.sort(key = lambda x: (-x[1], x[0]))
print(most[0][0])
