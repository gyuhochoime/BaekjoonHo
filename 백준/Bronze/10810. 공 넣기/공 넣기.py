import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
basket = [0] * n
for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().rstrip().split())
    for x in range(i - 1, j):
        basket[x] = k
for i in basket:
    print(i, end = " ")
