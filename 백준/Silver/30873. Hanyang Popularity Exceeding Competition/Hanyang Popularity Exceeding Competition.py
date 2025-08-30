import sys
n = int(sys.stdin.readline().rstrip())
arr = []
popul = 0
for i in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr.append((a, b))
for a, b in arr:
    if abs(a - popul) <= b:
        popul += 1
print(popul)
