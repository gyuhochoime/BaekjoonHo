import sys
def DFS(L):
    if L == m:
        for i in res:
            print(i, end = " ")
        print()
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                DFS(L + 1)
                ch[i] = 0
n, m = map(int, sys.stdin.readline().rstrip().split())
res = [0] * m
ch = [0] * (n + 1)
DFS(0)
