import sys
n, m, k = map(int, sys.stdin.readline().rstrip().split())
if n + m + k >= 100:
    print("OK")
else:
    if min(n, m, k) == n:
        print("Soongsil")
    elif min(n, m, k) == m:
        print("Korea")
    else:
        print("Hanyang")
