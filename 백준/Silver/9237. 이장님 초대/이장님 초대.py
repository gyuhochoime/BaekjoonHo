import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
namu = []
arr.sort(reverse = True)
for i in range(1, n + 1):
    namu.append(arr[i-1] + i)
namu.sort(reverse = True)
print(namu[0] + 1)
