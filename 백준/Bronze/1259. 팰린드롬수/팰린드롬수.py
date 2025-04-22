import sys
while True:
    n = sys.stdin.readline().rstrip()
    if n == "0":
        break
    m = len(n) // 2
    cnt = 0
    for i in range(m):
        if n[i] == n[len(n) - i - 1]:
            cnt += 1
    if cnt == m:
        print("yes")
    else:
        print("no")
