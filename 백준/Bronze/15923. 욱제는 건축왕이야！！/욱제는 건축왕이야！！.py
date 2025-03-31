import sys
T = int(sys.stdin.readline().rstrip())
arr = []
tot = 0
for i in range(T):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    arr.append(n)
    arr.append(m)
for j in range(T * 2):
    if arr[j - 2] > arr[j]:
        tot += arr[j - 2] - arr[j]
    elif arr[j - 2] < arr[j]:
        tot += arr[j] - arr[j - 2]
print(tot)
