import sys
n, m = map(int, sys.stdin.readline().split())
country = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
country.sort(key = lambda x: (-x[1], -x[2], -x[3]))
rank = 1
tmp = 0
prev_gold, prev_silver, prev_bronze = country[0][1], country[0][2], country[0][3]
country_rank = dict()
country_rank[country[0][0]] = rank
for i in range(1, n):
    if prev_gold == country[i][1] and prev_silver == country[i][2] and prev_bronze == country[i][3]:
        country_rank[country[i][0]] = rank
        tmp += 1
    else:
        rank += 1 + tmp
        tmp = 0
        country_rank[country[i][0]] = rank
    prev_gold, prev_silver, prev_bronze = country[i][1], country[i][2], country[i][3]
print(country_rank[m])
