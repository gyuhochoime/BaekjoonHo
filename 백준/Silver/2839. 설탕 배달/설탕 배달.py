import sys
n = int(sys.stdin.readline().rstrip())
if n == 4 or n == 7:
    print(-1)
else:
    if n % 5 == 1 or n % 5 == 3:
        print(n // 5 + 1)
    elif n % 5 == 2 or n % 5 == 4:
        print(n // 5 + 2)
    else:
        print(n // 5)
