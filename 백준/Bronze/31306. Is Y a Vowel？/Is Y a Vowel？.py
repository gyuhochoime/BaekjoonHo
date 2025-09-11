import sys
n = sys.stdin.readline().rstrip()
cnt = 0
cny = 0
for i in n:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        cnt += 1
        cny += 1
    elif i == "y":
        cny += 1
print(cnt, cny)
