import sys

n = int(sys.stdin.readline().rstrip())
for i in range(n):
    r, s = sys.stdin.readline().rstrip().split()
    for j in range(len(s)):
        print(int(r) * s[j], end = '')
    print()
