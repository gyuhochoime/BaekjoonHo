import sys
T = int(sys.stdin.readline().rstrip())
little = "ZZZ"
for i in range(T):
    n = sys.stdin.readline().rstrip()
    if len(n) == 3 and n < little:
        little = n
print(little)
