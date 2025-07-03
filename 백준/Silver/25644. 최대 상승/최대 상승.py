import sys
T = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
choi = 1000000001
tmp = 0
for i in arr:
    if i < choi:
        choi = i
    elif choi < i:
        tmp = max(i - choi, tmp)
print(tmp)
