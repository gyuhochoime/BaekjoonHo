import sys

cnt = 0
for line in sys.stdin:
    n = int(line.rstrip())
    if cnt <= 100:
        cnt += n
    if cnt > 100:
        if 100 - (cnt - n) >= cnt - 100:
            cnt = cnt
            break
        else:
            cnt = cnt - n
            break
print(cnt)

