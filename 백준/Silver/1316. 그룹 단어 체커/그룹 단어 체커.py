import sys
n = int(sys.stdin.readline().rstrip())
cnt = 0
for _ in range(n):
    a = list(sys.stdin.readline().rstrip())
    tmp = []
    for i in a:
        if i in tmp:
            if i != tmp[-1]:
                break
            else:
                tmp.append(i)
        else:
            tmp.append(i)
    else:
        cnt += 1
print(cnt)
