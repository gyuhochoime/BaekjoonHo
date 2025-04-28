import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    cnt = 0
    avg = (sum(arr) - arr[0]) / arr[0]
    for j in range(len(arr) - 1):
        if arr[j + 1] > avg:
            cnt += 1
    ratio = cnt / (len(arr) - 1) * 100
    print("%0.3f%%" % ratio)
