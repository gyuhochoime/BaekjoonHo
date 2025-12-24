import sys
n = int(sys.stdin.readline().rstrip())
star = 1
for i in range(n, n - 5, -1):
    star *= i
star //= 120
print(star)
