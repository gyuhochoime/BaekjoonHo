import sys
n = list(map(int, sys.stdin.readline().rstrip()))
cnt = 0
while True:
    if len(n) == 1:
        break
    n = list(map(int, str(sum(n))))
    cnt += 1
print(cnt)
for i in n:
    if i == 3 or i == 6 or i == 9:
        print("YES")
    else:
        print("NO")
