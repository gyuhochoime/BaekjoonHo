import sys
T = int(sys.stdin.readline())
max_tot = 0
for _ in range(T):
    n, m, k = map(int, sys.stdin.readline().split())
    if n == m and m == k and k == n:
        max_tot = max(max_tot, 10000 + n * 1000)
    elif n != m and m != k and k != n:
        max_tot = max(max_tot, max(n, m, k) * 100)
    else:
        if n == m:
            max_tot = max(max_tot, 1000 + n * 100)
        elif m == k:
            max_tot = max(max_tot, 1000 + m * 100)
        elif k == n:
            max_tot = max(max_tot, 1000 + k * 100)
print(max_tot)
