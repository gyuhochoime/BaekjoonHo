import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    jak = []
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in arr:
        if j % 2 == 0:
            jak.append(j)
    print(sum(jak), min(jak))
