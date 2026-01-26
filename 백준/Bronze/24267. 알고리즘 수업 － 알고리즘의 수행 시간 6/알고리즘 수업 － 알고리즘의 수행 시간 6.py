import sys
n = int(sys.stdin.readline().rstrip())
tot = 0
a, b = 0, 1
if n > 2:
    for _ in range(n - 2):
        a += b
        b += 1
        tot += a
print(tot)
print(3)
