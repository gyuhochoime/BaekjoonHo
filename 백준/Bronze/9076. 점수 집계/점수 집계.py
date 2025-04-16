import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    arr.sort()
    if arr[3] - arr[1] >= 4:
        print("KIN")
    else:
        print(arr[1] + arr[2] + arr[3])
