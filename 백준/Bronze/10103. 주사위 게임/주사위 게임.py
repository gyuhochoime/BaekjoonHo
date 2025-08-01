import sys
T = int(sys.stdin.readline().rstrip())
a = 100
b = 100
for i in range(T):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    if n > m:
        b -= n
    elif n < m:
        a -= m
print(a)
print(b)
