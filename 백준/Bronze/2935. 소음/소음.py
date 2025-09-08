import sys
n = int(sys.stdin.readline().rstrip())
m = sys.stdin.readline().rstrip()
k = int(sys.stdin.readline().rstrip())
if m == "+":
    print(n + k)
elif m == "*":
    print(n * k)
