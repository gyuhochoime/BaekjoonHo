import sys
n = int(sys.stdin.readline().rstrip())
print(n // 100 * 78, n - ((n // 100 * 20) // 100 * 22))
