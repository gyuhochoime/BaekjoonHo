import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
basket = [x for x in range(1, n + 1)]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    tmp = basket[i-1:j]
    tmp.reverse()
    basket[i-1:j] = tmp
for i in basket:
    print(i, end = " ")
