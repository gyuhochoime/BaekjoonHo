import sys
T = int(sys.stdin.readline().rstrip())
a = b = c = d = 0
for i in range(T):
    n, m, k = map(int, sys.stdin.readline().rstrip().split())
    if n == 1:
        d += 1
    elif n != 1 and m == 1 or m == 2:
        a += 1
    elif n != 1 and m == 3:
        b += 1
    elif n != 1 and m == 4:
        c += 1
print(a)
print(b)
print(c)
print(d)
