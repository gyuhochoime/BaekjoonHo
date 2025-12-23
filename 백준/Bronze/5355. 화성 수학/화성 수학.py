import sys
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    a = list(map(str, sys.stdin.readline().rstrip().split()))
    su = float(a[0])
    for i in range(1, len(a)):
        if a[i] == "@":
            su *= 3
        elif a[i] == "%":
            su += 5
        elif a[i] == "#":
            su -= 7
    print("%.2f" % su)
