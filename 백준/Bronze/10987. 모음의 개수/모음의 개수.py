import sys
n = list(sys.stdin.readline().rstrip())
moum = "aeiou"
tot = 0
for i in range(len(n)):
    if n[i] in moum:
        tot += 1
print(tot)
