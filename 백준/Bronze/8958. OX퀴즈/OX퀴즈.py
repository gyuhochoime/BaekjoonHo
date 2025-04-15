import sys
T = int(sys.stdin.readline().rstrip())
arr = []
for i in range(T):
    tot = 0
    cnt = 0
    n = list(sys.stdin.readline().rstrip())
    for j in range(len(n)):
        if n[j] == "O":
            cnt += 1
            tot += cnt
        elif n[j] == "X":
            cnt = 0
    print(tot)
