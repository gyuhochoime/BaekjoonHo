import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
h = list(map(int, sys.stdin.readline().rstrip().split()))
a = list(map(int, sys.stdin.readline().rstrip().split()))

helmet = 0
armor = 0
for i in range(n):
    helmet = max(h)
for j in range(m):
    armor = max(a)
print(helmet + armor)
