import sys
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    tot = 0
    a, b = map(int, sys.stdin.readline().rstrip().split())
    for i in range(a, b + 1):
        for j in str(i):
            if j == "0":
                tot += 1
    print(tot)
