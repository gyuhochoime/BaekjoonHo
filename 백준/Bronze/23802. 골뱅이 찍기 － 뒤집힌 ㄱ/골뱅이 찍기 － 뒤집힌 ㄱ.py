import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    print("@" * 5 * n)
for i in range(n * 4):
    print("@" * n)
