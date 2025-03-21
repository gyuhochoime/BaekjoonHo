import sys
while True:
    n = sys.stdin.readline().rstrip()
    cnt = 0
    if n == "#":
        break
    for i in n:
        if i in "aeiouAEIOU":
            cnt += 1
    print(cnt)
print()
