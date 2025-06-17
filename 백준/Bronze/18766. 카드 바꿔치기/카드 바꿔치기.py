import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    n = int(sys.stdin.readline().rstrip())
    arn = list(map(str, sys.stdin.readline().rstrip().split()))
    arm = list(map(str, sys.stdin.readline().rstrip().split()))
    arn.sort()
    arm.sort()
    if arn == arm:
        print("NOT CHEATER")
    else:
        print("CHEATER")
