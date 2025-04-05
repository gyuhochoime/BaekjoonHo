import sys
n = int(sys.stdin.readline().rstrip())
m = list(sys.stdin.readline().rstrip())
arr = []
for i in range(n):
    if m[i] == "I":
        arr.append("i")
    elif m[i] == "l":
        arr.append("L")
for i in range(len(arr)):
    print(arr[i], end = "")
