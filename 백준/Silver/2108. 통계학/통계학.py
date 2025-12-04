import sys
n = int(sys.stdin.readline().rstrip())
su = []
da = dict()
for _ in range(n):
    a = int(sys.stdin.readline().rstrip())
    su.append(a)
    if a in da:
        da[a] += 1
    else:
        da[a] = 1
su.sort()
dabin = [(key, value) for key, value in da.items()]
dabin.sort(key = lambda x: (-x[1], x[0]))
print(int(round(sum(su) / n, 0)))
print(su[n//2])
if n > 1 and dabin[0][1] == dabin[1][1]:
    print(dabin[1][0])
else:
    print(dabin[0][0])
print(abs(su[-1] - su[0]))
