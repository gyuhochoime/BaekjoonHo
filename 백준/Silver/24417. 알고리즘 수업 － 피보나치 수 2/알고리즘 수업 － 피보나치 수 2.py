import sys
n = int(sys.stdin.readline())
a, b = 1, 1
for i in range(2, n):
    a, b = b, (a + b) % 1000000007
print(b, n - 2)
