import sys
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    a = sys.stdin.readline().rstrip()
    tot = 0
    for i in a:
        if i != " ":
            tot += ord(i) - 64
    if tot == 100:
        print("PERFECT LIFE")
    else:
        print(tot)
