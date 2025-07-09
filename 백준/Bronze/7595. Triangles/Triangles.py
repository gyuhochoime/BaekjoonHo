import sys
while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    for i in range(1, n + 1):
        print("*" * i)
