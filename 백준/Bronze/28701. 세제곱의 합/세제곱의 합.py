import sys
n = int(sys.stdin.readline().rstrip())
a = [x for x in range(1, n + 1)]
tot = sum(a)
jae = tot ** 2
sae = 0
for i in a:
    sae += i ** 3
print(tot)
print(jae)
print(sae)
