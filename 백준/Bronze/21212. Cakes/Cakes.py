import sys
ing = []
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    ing.append(b // a)
print(min(ing))
