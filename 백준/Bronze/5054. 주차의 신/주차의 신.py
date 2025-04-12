import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    arr.sort()
    parking = (arr[0] + arr[n-1]) // 2
    print((parking - arr[0] + arr[n-1] - parking) * 2)
