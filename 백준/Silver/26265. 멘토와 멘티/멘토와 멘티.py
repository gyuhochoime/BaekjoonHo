import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    a, b = map(str, sys.stdin.readline().rstrip().split())
    arr.append((a, b))
arr.sort(key = lambda x: x[1], reverse = True)
arr.sort(key = lambda x: x[0])
for key, value in arr:
    print(key, value)
