import sys
while True:
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == 0 and b == 0 and c == 0:
        break
    if c - b == b - a:
        print("AP %d" % (c + (b - a)))
    else:
        print("GP %d" % (c * (b // a)))
