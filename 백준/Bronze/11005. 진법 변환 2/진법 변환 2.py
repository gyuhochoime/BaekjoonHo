import sys
zin = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n, b = map(int, sys.stdin.readline().rstrip().split())
bub = ""
while n != 0:
    bub += zin[n%b]
    n //= b
print(bub[::-1])
