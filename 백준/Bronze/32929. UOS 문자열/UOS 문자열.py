import sys
n = int(sys.stdin.readline())
a = n % 3
if a == 0:
    print("S")
elif a == 1:
    print("U")
else:
    print("O")
