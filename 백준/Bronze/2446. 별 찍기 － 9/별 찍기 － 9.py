import sys
n = int(sys.stdin.readline().rstrip())
for i in range(2 * n - 1, 0, -2):
    print(" " * (n - ((i + 1) // 2)) + "*" * i)
for i in range(3, 2 * n, 2):
    print(" " * (n - ((i + 1) // 2)) + "*" * i)
