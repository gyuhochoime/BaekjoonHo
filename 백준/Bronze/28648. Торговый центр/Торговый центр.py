import sys
n = int(sys.stdin.readline().rstrip())
arr = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr.append(a + b)
arr.sort()
print(arr[0])
