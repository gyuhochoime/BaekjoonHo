import sys
a = list(map(int, sys.stdin.readline().rstrip().split()))
tot = 0
for i in a:
    if i == 1:
        tot += 500
    elif i == 2:
        tot += 800
    elif i == 3:
        tot += 1000
print(5000 - tot)
