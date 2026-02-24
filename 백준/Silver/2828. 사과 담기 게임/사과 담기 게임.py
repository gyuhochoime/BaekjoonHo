import sys
n, m = map(int, sys.stdin.readline().split())
j = int(sys.stdin.readline())
basket = [int(sys.stdin.readline()) for _ in range(j)]
lt = 1
rt = m
tot = 0
for i in basket:
    if i > rt:
        a = i - rt
        tot += a
        lt += a
        rt += a
    elif i < lt:
        a = lt - i
        tot += a
        lt -= a
        rt -= a
print(tot)
