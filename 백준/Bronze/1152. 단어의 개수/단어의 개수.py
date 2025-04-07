import sys
n = list(map(str, sys.stdin.readline().rstrip()))
tot = 0
if len(n) == 0:
    print(0)
else:
    for i in range(len(n)):
        if n[i] == " ":
            tot += 1
    if n[0] == " ":
        tot -= 1
    if n[len(n)-1] == " ":
        tot -= 1
    print(tot + 1)
