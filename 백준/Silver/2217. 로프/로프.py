import sys
n = int(sys.stdin.readline())
rope = sorted([int(sys.stdin.readline()) for _ in range(n)])
weight = []
for i in rope:
    weight.append(i * n)
    n -= 1
print(max(weight))
