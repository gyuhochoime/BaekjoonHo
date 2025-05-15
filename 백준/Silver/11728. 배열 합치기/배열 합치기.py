import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
first = list(map(int, sys.stdin.readline().rstrip().split()))
second = list(map(int, sys.stdin.readline().rstrip().split()))
arr = []
for i in range(n):
    arr.append(first[i])
for i in range(m):
    arr.append(second[i])
arr.sort()
for i in arr:
    print(i, end = " ")
