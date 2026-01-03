import sys
while True:
    a = sys.stdin.readline().rstrip()
    if a == "#":
        break
    alpha = a[0]
    cpr = a.lower()
    cnt = 0
    for i in range(2, len(a)):
        if cpr[i] == cpr[0]:
            cnt += 1
    print(alpha, cnt)
