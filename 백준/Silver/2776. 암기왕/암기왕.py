import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    n = int(sys.stdin.readline().rstrip())
    arn = list(map(int, sys.stdin.readline().rstrip().split()))
    m = int(sys.stdin.readline().rstrip())
    arm = list(map(int, sys.stdin.readline().rstrip().split()))
    dic1 = {}
    for i in arn:
        dic1[i] = 1
    for i in arm:
        if i in dic1:
            print(dic1[i])
        else:
            print(0)
