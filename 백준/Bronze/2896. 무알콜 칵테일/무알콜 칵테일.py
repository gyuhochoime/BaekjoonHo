import sys
amount = list(map(int, sys.stdin.readline().rstrip().split()))
ratio = list(map(int, sys.stdin.readline().rstrip().split()))
a = amount[0] / ratio[0]
b = amount[1] / ratio[1]
c = amount[2] / ratio[2]
m = min(a, b, c)
print(amount[0] - ratio[0] * m, amount[1] - ratio[1] * m, amount[2] - ratio[2] * m)
