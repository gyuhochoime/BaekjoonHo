import sys
n = int(sys.stdin.readline().rstrip())
m = "@" * 5 * n
k = "@" * n + " " * 3 * n + "@" * n
for i in range(n):
    print(m)
for i in range(n):
    print(k)
for i in range(n):
    print(k)
for i in range(n):
    print(k)
for i in range(n):
    print(m)
