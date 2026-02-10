import sys
n = int(sys.stdin.readline())
if n % 7 != 0 and "7" not in str(n):
    print(0)
elif n % 7 == 0 and "7" not in str(n):
    print(1)
elif n % 7 != 0 and "7" in str(n):
    print(2)
elif n % 7 == 0 and "7" in str(n):
    print(3)
