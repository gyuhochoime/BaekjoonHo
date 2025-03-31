import sys
a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
c = int(sys.stdin.readline().rstrip())
d = int(sys.stdin.readline().rstrip())
p = int(sys.stdin.readline().rstrip())

x = a * p
y = b + max(0, p - c) * d

print(min(x, y))
