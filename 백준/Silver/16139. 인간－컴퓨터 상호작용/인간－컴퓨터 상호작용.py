import sys
moonja  = sys.stdin.readline().strip()
num = int(sys.stdin.readline())
alpha = [[0] * len(moonja) for _ in range(26)]
for i in range(len(moonja)):
    a = ord(moonja[i]) - 97
    alpha[a][i] = 1
for _ in range(num):
    moon, lt, rt = map(str, sys.stdin.readline().strip().split())
    cnt = 0
    bet = ord(moon) - 97
    for i in range(int(lt), int(rt) + 1):
        if alpha[bet][i] == 1:
            cnt += 1
    print(cnt)
