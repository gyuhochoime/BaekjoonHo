import sys
n = int(sys.stdin.readline())
stick = 64
long_stick = 0
while stick > 0:
    long_stick += n // stick
    n %= stick
    stick //= 2
print(long_stick)
