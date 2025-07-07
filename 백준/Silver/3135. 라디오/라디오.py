import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    k = int(sys.stdin.readline().rstrip())
    arr.append(k)
arr.sort()
ju = abs(n - m)
for i in arr:
    ju = min(ju, abs(i - m) + 1)
print(ju)
