import sys

n = int(sys.stdin.readline().rstrip())
m = "@" * n + " " * 3 * n + "@" * n
k = "@" * 5 * n
for i in range(2 * n):
    print(m)
for j in range(n):
    print(k)
for s in range(n):
    print(m)
for z in range(n):
    print(k)
