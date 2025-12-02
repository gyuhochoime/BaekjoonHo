import sys
def DFS(L):
    if L == m:
        for j in res:
            print(j, end = " ")
        print()
    else:
        for i in range(1, n + 1):
            res[L] = i
            DFS(L+1)
n, m = map(int, sys.stdin.readline().rstrip().split())
res = [0] * m
DFS(0)
