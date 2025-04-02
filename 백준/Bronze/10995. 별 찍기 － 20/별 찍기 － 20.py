import sys
n = int(sys.stdin.readline().rstrip())
m = ("*" + " ") * n
k = (" " + "*") * n
for i in range(n):
    if i % 2 == 0:
        print(m)
    elif i % 2 == 1:
        print(k)
