import sys
square = []
a = 3
for _ in range(15):
    square.append(a ** 2)
    a += a - 1
n = int(sys.stdin.readline())
print(square[n-1])
