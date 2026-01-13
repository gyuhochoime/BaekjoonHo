import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
son = {1: 0, 2: 0, 3: 0}
for i in arr:
    son[i] += 1
tul = [(key, value) for key, value in son.items()]
tul.sort(key = lambda x: (x[1]))
print(tul[0][0])
print(tul[-1][0])