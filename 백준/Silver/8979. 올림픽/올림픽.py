import sys
n, m = map(int, sys.stdin.readline().split())
country = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
country.sort(key = lambda x: (-x[1], -x[2], -x[3]))
rank = 1
prev_gold, prev_silver, prev_bronze = country[0][1], country[0][2], country[0][3]
country_rank = dict()
for num, gold, silver, bronze in country:
    if prev_gold == gold and prev_silver == silver and prev_bronze == bronze:
        country_rank[num] = rank
    else:
        rank += 1
        country_rank[num] = rank
    prev_gold, prev_silver, prev_bronze = gold, silver, bronze
print(country_rank[m])
