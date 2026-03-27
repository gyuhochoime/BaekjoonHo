import sys
n = int(sys.stdin.readline())
seven_zero_sea = []
for _ in range(n):
    a = float(sys.stdin.readline())
    seven_zero_sea.append(a)
seven_zero_sea.sort()
for i in range(7):
    print("%.3f" % seven_zero_sea[i])