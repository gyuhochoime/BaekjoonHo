import sys
n = int(sys.stdin.readline().rstrip())
while n % 2 == 0 and n // 2 > 0:
    n = n // 2
if n == 1:
    print(1)
else:
    print(0)
