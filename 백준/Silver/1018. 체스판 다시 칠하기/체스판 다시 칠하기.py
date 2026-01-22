import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
chess = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]
fir = "B"
sec = "W"
mini = 2100000000
x = n - 7
y = m - 7
for i in range(x):
    a = ""
    for j in range(y):
        cnt = 0
        for k in range(i, i + 8):
            if k % 2 == 0:
                a = fir
            else:
                a = sec
            for r in range(j, j + 8):
                if chess[k][r] != a:
                    cnt += 1
                if a == fir:
                    a = sec
                elif a == sec:
                    a = fir
        if cnt > 31:
            cnt = 64 - cnt
        mini = min(mini, cnt)
print(mini)
