import sys
def DFS(L):
    if L == m:
        for j in range(m):
            print(res[j], end = " ")
        print()
    else:
        for i in range(n):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = arr[i]
                DFS(L + 1)
                ch[i] = 0
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
res = [0] * m
ch = [0] * n
DFS(0)
