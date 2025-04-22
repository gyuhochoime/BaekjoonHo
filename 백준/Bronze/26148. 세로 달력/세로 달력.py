import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print(30)
else:
    print(29)
