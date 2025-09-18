import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    n = int(sys.stdin.readline().rstrip())
    if n % 2 == 0:
        print("even")
    else:
        print("odd")
