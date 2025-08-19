import sys
n = list(map(str, sys.stdin.readline().rstrip()))
a = len(n)
b = 0
c = 0
for i in n:
    if i == ":":
        b += 1
    elif i == "_":
        c += 1
c = c * 5
print(a + b + c)
