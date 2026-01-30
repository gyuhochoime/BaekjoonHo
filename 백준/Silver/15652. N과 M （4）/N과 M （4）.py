import sys
def DFS(L, s):
    if L == m:
        for j in range(L):
            print(res[j], end = " ")
        print()
    else:
        for i in range(s, n + 1):
            res[L] = i
            DFS(L + 1, i)
n, m = map(int, sys.stdin.readline().split())
res = [0] * m
DFS(0, 1)
