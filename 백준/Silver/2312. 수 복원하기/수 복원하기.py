import sys
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    a = 2
    arr = []
    while n > 1:
        su = a
        cnt = 0
        while n % a == 0:
            n //= a
            cnt += 1
        if cnt > 0:
            arr.append((su, cnt))
        a += 1
    for i in arr:
        print(*i)
    a = 2
