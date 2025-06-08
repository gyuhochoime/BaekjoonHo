import sys
T = int(sys.stdin.readline().rstrip())
arr = []
for i in range(T):
    n = int(sys.stdin.readline().rstrip())
    arr.append(n)
arr.sort()
for i in arr:
    print(i)
