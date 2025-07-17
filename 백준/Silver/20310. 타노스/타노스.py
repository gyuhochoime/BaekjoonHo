import sys
n = list(map(int, sys.stdin.readline().rstrip()))
arr = [0] * 2
arm = []
for i in n:
    if i == 0:
        arr[0] += 1
    else:
        arr[1] += 1
for i in range(len(arr)):
    arr[i] = arr[i] // 2
    arm.append(arr[i] * str(i))
arm.sort()
for i in arm:
    print(i, end = "")
