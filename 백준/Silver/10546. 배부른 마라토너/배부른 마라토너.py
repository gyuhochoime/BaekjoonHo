import sys
n = int(sys.stdin.readline().rstrip())
arr = dict()
mar = []
for i in range(n * 2 - 1):
    a = sys.stdin.readline().rstrip()
    if a in arr:
        if arr[a] == 1:
            arr[a] = 0
        elif arr[a] == 0:
            arr[a] = 1
    else:
        arr[a] = 1
for key, val in arr.items():
    mar.append((key, val))
mar.sort(key = lambda x: -x[1])
print(mar[0][0])
