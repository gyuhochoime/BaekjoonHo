import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    print("@" * n + " " * 3 * n + "@" * n)
for i in range(n):
    print("@" * n + " " * 2 * n + "@" * n)
for i in range(n):
    print("@" * 3 * n)
for i in range(n):
    print("@" * n + " " * 2 * n + "@" * n)
for i in range(n):
    print("@" * n + " " * 3 * n + "@" * n)
