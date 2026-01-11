import sys
while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    a = str(n)
    while len(a) > 1:
        tmp = 0
        for i in a:
            tmp += int(i)
        a = str(tmp)
    print(a)
