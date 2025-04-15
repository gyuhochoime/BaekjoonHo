import sys
while True:
    n, m, k = map(int, sys.stdin.readline().rstrip().split())
    if n == 0 and m == 0 and k == 0:
        break
    if n ** 2 + m ** 2 == k ** 2 or n ** 2 + k ** 2 == m ** 2 or k ** 2 + m ** 2 == n ** 2:
        print("right")
    else:
        print("wrong")
