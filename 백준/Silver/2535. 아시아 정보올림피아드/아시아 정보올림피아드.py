import sys
n = int(sys.stdin.readline())
medal = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
medal.sort(key = lambda x: (-x[2]))
dic = dict()
cnt = 0
for con, num, score in medal:
    if con in dic:
        dic[con] += 1
    else:
        dic[con] = 1
    if dic[con] > 2:
        continue
    else:
        print(con, num)
        cnt += 1
        if cnt == 3:
            break
