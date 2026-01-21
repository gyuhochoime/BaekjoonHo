import sys
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    a = int(sys.stdin.readline().rstrip())
    qua = dim = nic = pen = 0
    if a >= 25:
        qua = a // 25
        a %= 25
    if a >= 10:
        dim = a // 10
        a %= 10
    if a >= 5:
        nic = a // 5
        a %= 5
    if a >= 1:
        pen = a
    print(qua, dim, nic, pen)
