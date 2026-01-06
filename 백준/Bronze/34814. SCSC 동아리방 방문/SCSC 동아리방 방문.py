import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
drink = list(map(int, sys.stdin.readline().rstrip().split()))
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if max(drink) == drink[b-1]:
        continue
    else:
        drink[a-1] -= 1
for i in drink:
    print(i, end = " ")
