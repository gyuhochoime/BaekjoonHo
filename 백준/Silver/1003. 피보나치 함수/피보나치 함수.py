import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    a, b = 1, 0
    for _ in range(n):
        a, b = b, a + b
    print(a, b)
