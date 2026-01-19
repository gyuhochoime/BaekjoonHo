import sys
n = int(sys.stdin.readline().rstrip())
for i in range(1, n + 1):
    tmp = 0
    a = str(i)
    for x in a:
        tmp += int(x)
    tmp += i
    if tmp == n:
        print(a)
        break
else:
    print(0)
