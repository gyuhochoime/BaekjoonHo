import sys
dic = dict()
team = []
alpha = []
for _ in range(3):
    n, m, k = map(str, sys.stdin.readline().rstrip().split())
    team.append(int(m) % 100)
    dic[k] = int(n)
a = [(key, value) for key, value in dic.items()]
a.sort(key = lambda x: (-x[1]))
for key, value in a:
    alpha.append(key[0])
team.sort()
for i in team:
    print(i, end = "")
print()
for i in alpha:
    print(i, end = "")
