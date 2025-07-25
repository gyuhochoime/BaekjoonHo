import sys
n = int(sys.stdin.readline().rstrip())
arr = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr.append((a, b))
arr.sort(reverse = True)
tot = 0
for o, c in arr:
    if n > 0:
        tot += o * n + c
        n -= 1
print(tot)
