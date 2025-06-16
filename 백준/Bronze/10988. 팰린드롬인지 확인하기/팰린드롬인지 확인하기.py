import sys
n = sys.stdin.readline().rstrip()
for i in range(len(n) // 2):
    if n[i] != n[len(n) - 1 - i]:
        print(0)
        break
else:
    print(1)
