import sys
T = int(sys.stdin.readline().rstrip())
arr = []
for i in range(T):
    n, m = map(str, sys.stdin.readline().rstrip().split())
    arr.append([int(n), m])
arr.sort(key = lambda x : [x[0]])
for i in range(T):
    for j in range(2):
        print(arr[i][j], end = " ")
    print()
