import sys
n = int(sys.stdin.readline().rstrip())
arn = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
arm = list(map(int, sys.stdin.readline().rstrip().split()))
dic1 = {}
for i in arn:
    if i in dic1:
        dic1[i] += 1
    else:
        dic1[i] = 1
for i in range(m):
    if arm[i] in dic1:
        print(dic1[arm[i]], end = " ")
    else:
        print(0, end = " ")
