import sys
n = int(sys.stdin.readline().rstrip())
coin = [500, 100, 50, 10, 5, 1]
cnt = 0
jan = 1000 - n
for i in coin:
    while jan >= i:
        jan -= i
        cnt += 1
print(cnt)
