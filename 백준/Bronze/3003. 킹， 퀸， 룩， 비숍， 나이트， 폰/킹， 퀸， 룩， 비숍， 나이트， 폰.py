import sys
arr = list(map(int, sys.stdin.readline().rstrip().split()))
chess = [1, 1, 2, 2, 2, 8]
for i in range(len(arr)):
    print(chess[i] - arr[i], end = " ")
