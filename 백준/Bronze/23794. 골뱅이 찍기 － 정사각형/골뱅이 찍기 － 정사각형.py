import sys
n = int(sys.stdin.readline().rstrip())
print("@" * (n + 2))
for i in range(n):
    print("@" + " " * n + "@")
print("@" * (n + 2))
