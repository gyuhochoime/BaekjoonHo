import sys
n = list(sys.stdin.readline().rstrip())
tot = []
for i in range(len(n)):
    if ord(n[i]) >= 65 and ord(n[i]) <= 90:
        tot.append(n[i])
for i in tot:
    print(i, end = "")
