import sys
n = int(sys.stdin.readline().rstrip())
m = "@" * 3 * n + " " * n + "@" * n
k = "@" * n + " " * n + "@" * n + " " * n + "@" * n
s = "@" * n + " " * n + "@" * 3 * n
for i in range(n):
    print(m)
for i in range(n):
    print(k)
for i in range(n):
    print(k)
for i in range(n):
    print(k)
for i in range(n):
    print(s)
