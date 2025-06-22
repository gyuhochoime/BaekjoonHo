import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    arr = list(sys.stdin.readline().rstrip())
    print(arr[0]+arr[len(arr)-1])
