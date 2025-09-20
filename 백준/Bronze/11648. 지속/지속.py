import sys
n = sys.stdin.readline().rstrip()
cnt = 0
while len(n) > 1:
    tmp = 1
    for i in n:
        tmp *= int(i)
    n = str(tmp)
    cnt += 1
print(cnt)
