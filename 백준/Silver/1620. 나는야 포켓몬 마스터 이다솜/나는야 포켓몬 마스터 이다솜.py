import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
name = dict()
order = dict()
for i in range(1, n + 1):
    a = sys.stdin.readline().rstrip()
    name[i] = a
    order[a] = i
for i in range(m):
    a = sys.stdin.readline().rstrip()
    if a.isdigit():
        print(name[int(a)])
    else:
        print(order[a])
