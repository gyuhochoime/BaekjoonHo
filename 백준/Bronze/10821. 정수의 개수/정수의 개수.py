import sys
n = list(sys.stdin.readline().rstrip())
tnt = 0
for i in n:
    if i == ",":
        tnt += 1
print(tnt + 1)
