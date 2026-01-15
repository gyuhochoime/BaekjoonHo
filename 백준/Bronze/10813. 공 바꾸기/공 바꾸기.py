import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
basket = [x for x in range(1, n + 1)]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    tmp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = tmp
for i in basket:
    print(i, end = " ")
