import sys
T = int(sys.stdin.readline().rstrip())
arr = []
for i in range(T):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    arr.append(n * m)
print(max(arr))
