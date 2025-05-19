import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
tmp = []
for i in range(n):
    tmp.append(arr[i]+arr[n*2-1-i])
print(min(tmp))
