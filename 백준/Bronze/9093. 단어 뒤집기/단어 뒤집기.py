import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    arr = list(map(str, sys.stdin.readline().rstrip().split()))
    for i in range(len(arr)):
        arr[i] = arr[i][::-1]
    for j in arr:
        print(j, end = " ")
    print()
