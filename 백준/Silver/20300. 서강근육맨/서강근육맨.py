import sys
T = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
if T % 2 == 1:
    gun = arr[T-1]
    for i in range(len(arr) // 2):
        gun = max(gun, arr[i] + arr[T - 2 - i])
    print(gun)
else:
    gun = 0
    for i in range(len(arr) // 2):
        gun = max(gun, arr[i] + arr[T - 1 - i])
    print(gun)
