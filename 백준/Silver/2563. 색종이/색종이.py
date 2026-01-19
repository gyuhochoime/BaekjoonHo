import sys
n = int(sys.stdin.readline().rstrip())
arr = [[0] * 101 for _ in range(101)]
extent = 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            arr[i][j] = 1
for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            extent += 1
print(extent)
