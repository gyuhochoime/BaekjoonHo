import sys
T = int(sys.stdin.readline().rstrip())
arr = []
for i in range(T):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    arr.append([n, m])
arr.sort(key = lambda x: (x[1], x[0]))
for i in arr:
    print(i[0], i[1])
