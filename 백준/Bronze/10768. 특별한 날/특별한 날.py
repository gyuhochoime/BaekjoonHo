import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
if n == 2 and m == 18:
    print("Special")
elif n == 2 and m <= 18:
    print("Before")
elif n <= 1 and m <= 31:
    print("Before")
else:
    print("After")
