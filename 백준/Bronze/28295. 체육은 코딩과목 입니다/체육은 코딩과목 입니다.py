import sys
tot = 0
for i in range(10):
    n = int(sys.stdin.readline().rstrip())
    tot += n
if tot % 4 == 0:
    print("N")
elif tot % 4 == 1:
    print("E")
elif tot % 4 == 2:
    print("S")
elif tot % 4 == 3:
    print("W")
