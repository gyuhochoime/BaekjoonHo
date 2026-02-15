import sys
arr = [[0] * 101 for _ in range(101)]
tot = 0
for _ in range(4):
    n, m, k, r = map(int, sys.stdin.readline().split())
    for i in range(n, k):
        for j in range(m, r):
            if arr[i][j] == 0:
                arr[i][j] = 1
for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            tot += 1
print(tot)
