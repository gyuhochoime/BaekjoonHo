import sys

n = list(map(int, sys.stdin.readline().rstrip().split()))
asc = 0
for i in range(len(n) - 1):
    if n[i] < n[i + 1]:
        asc += 1
    elif n[i] > n[i + 1]:
        asc -= 1
if asc == len(n) - 1:
    print("ascending")
elif asc == -(len(n) - 1):
    print("descending")
else:
    print("mixed")
