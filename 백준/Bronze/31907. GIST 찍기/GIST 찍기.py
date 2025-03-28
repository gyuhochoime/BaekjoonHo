import sys
n = int(sys.stdin.readline().rstrip())
m = "G..."
k = ".I.T"
r = "..S."
for i in range(n):
    print(m[0] * n + m[1] * n + m[2] * n + m[3] * n)
for j in range(n):
    print(k[0] * n + k[1] * n + k[2] * n + k[3] * n)
for s in range(n):
    print(r[0] * n + r[1] * n + r[2] * n + r[3] * n)
