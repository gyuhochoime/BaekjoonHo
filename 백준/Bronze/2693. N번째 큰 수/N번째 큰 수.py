import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    arr.sort(reverse = True)
    print(arr[2])
