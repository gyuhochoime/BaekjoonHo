import sys
def sol(num):
    lt = 0
    rt = len(arr) - 1
    while lt <= rt:
        mid = (lt + rt) // 2
        if arr[mid][1] >= num:
            rt = mid - 1
        else:
            lt = mid + 1
    return arr[lt][0] 
n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    a, b = map(str, sys.stdin.readline().rstrip().split())
    arr.append((a, int(b)))
for _ in range(m):
    num = int(sys.stdin.readline())
    print(sol(num))