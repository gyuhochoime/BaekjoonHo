import sys
while True:
    n, m, k = map(str, sys.stdin.readline().rstrip().split())
    if n == "#" and m == "0" and k == "0":
        break
    if int(m) > 17 or int(k) >= 80:
        print(n, "Senior")
    else:
        print(n, "Junior")
