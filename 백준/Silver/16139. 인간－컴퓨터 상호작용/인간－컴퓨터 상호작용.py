import sys
moonja  = sys.stdin.readline().strip()
num = int(sys.stdin.readline())
alpha = [[0] * (len(moonja) + 1) for _ in range(26)]
for i in range(26):
    for j in range(len(moonja)):
        alpha[i][j+1] = alpha[i][j]
        if ord(moonja[j]) - 97 == i:
            alpha[i][j+1] += 1
for _ in range(num):
    moon, lt, rt = map(str, sys.stdin.readline().strip().split())
    bet = ord(moon) - 97
    print(alpha[bet][int(rt)+1] - alpha[bet][int(lt)])
