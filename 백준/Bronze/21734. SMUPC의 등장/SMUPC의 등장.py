import sys
n = list(sys.stdin.readline().rstrip())
for i in n:
    a = list(str(ord(i)))
    tot = 0
    for j in a:
        tot += int(j)
    print(tot * i)
