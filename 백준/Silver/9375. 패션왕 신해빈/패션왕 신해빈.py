import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    fas = dict()
    n = int(sys.stdin.readline().rstrip())
    for _ in range(n):
        a, b = map(str, sys.stdin.readline().rstrip().split())
        if b in fas:
            fas[b] += 1
        else:
            fas[b] = 1
    comb = [(key, value) for key, value in fas.items()]
    tot = 1
    for key, value in comb:
        tot *= (value + 1)
    print(tot - 1)
