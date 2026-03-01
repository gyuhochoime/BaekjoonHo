import sys
n = list(map(str, sys.stdin.readline().rstrip()))
for i in range(len(n)):
    if ord(n[i]) <= 90:
        n[i] = n[i].lower()
    else:
        n[i] = n[i].upper()
for i in n:
    print(i, end = "")
