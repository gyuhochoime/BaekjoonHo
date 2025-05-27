import sys
n = list(map(int, sys.stdin.readline().rstrip()))
if 0 in n and sum(n) % 3 == 0:
    n.sort(reverse = True)
    for i in n:
        print(i, end = "")
else:
    print(-1)
