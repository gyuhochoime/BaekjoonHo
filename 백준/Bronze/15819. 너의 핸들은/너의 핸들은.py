import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
for i in range(n):
    a = sys.stdin.readline().rstrip()
    arr.append(a)
arr.sort()
print(arr[m - 1])
