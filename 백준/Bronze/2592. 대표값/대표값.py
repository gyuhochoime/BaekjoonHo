import sys
su = dict()
tot = 0
for _ in range(10):
    n = int(sys.stdin.readline().rstrip())
    if n in su:
        su[n] += 1
    else:
        su[n] = 1
    tot += n
avg = tot // 10
been = [(key, value) for key, value in su.items()]
been.sort(key = lambda x: (-x[1]))
print(avg)
print(been[0][0])
