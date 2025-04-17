import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
black = []
tot = 21435678
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            black.append(arr[i] + arr[j] + arr[k])
for i in black:
    if abs(m - i) < abs(tot - m) and i <= m:
        tot = i
print(tot)
