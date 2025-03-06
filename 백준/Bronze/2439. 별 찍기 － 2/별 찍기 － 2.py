import sys

n = int(sys.stdin.readline().rstrip())
k = n
for i in range(1, n + 1):
    print((" " * (k - i)) + "*" * i)
