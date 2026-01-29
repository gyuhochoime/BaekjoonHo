import sys
def DFS(L, s):
    if L == m:
        for j in range(L):
            print(arr[j], end = " ")
        print()
    else:
        for i in range(s, n + 1):
            arr[L] = i
            DFS(L + 1, i + 1)
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = [0] * (n + 1)
DFS(0, 1)
