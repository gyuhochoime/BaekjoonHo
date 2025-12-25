import sys
n = int(sys.stdin.readline().rstrip())
cnt = 0
money = n
while True:
    if len(str(money * 2)) == len(str(money)):
        cnt += 1
        money *= 2
    else:
        break
print(cnt)
