import sys
n = int(sys.stdin.readline().rstrip())
m = "@" * 5 * n
k = "@" * n
for i in range(n):
    print(m)
for j in range(n):
    print(k)
for i in range(n):
    print(m)
for j in range(n):
    print(k)
for i in range(n):
    print(m)
