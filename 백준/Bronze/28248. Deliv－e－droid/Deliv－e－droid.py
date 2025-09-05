import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
if n > m:
    print(n * 50 - m * 10 + 500)
else:
    print(n* 50 - m * 10)
