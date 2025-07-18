import sys
n = list(map(str, sys.stdin.readline().rstrip()))
for i in range(len(n)):
    if n[i] == "e":
        n[i] = n[i] * 2
for i in n:
    print(i, end = "")
