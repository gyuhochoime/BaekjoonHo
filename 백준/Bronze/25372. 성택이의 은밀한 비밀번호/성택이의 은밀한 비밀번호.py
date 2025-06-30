import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    n = sys.stdin.readline().rstrip()
    if len(n) >= 6 and len(n) <= 9:
        print("yes")
    else:
        print("no")
