import sys
n = int(sys.stdin.readline().rstrip())
a = 0
b = 1
if n == 1:
    print(a, b)
else:
    for i in range(n - 1):
        b = a + b
        a = b - a
    print(a, b)
    
