import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
while True:
    a = -sum(arr)
    if a > arr[0]:
        arr[0] = a
        arr.sort()
    elif a <= arr[0]:
        print(sum(arr))
        break
