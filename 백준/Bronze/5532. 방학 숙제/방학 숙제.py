import sys
l = int(sys.stdin.readline().rstrip())
a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
c = int(sys.stdin.readline().rstrip())
d = int(sys.stdin.readline().rstrip())
math = a // c
korean = b // d
if a % c > 0:
    math += 1
if b % d > 0:
    korean += 1
print(l - max(math, korean))
