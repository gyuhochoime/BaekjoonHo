import sys
n = int(sys.stdin.readline().rstrip())
m = "@" * n + " " * 3 * n + "@" * n
k = "@" * 5 * n
for i in range(n):
    print(m)
for i in range(n):
    print(k)
for i in range(n):
    print(m)
for i in range(n):
    print(k)
for i in range(n):
    print(m)
