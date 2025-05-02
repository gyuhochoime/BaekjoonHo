import sys
T = int(sys.stdin.readline().rstrip())
divisor = list(map(int, sys.stdin.readline().rstrip().split()))
divisor.sort(reverse = True)
print(divisor[0] * divisor[T - 1])
