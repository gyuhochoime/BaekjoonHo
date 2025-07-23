import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
mat = {}
for i in arr:
    if i in mat:
        mat[i] += 1
    else:
        mat[i] = 1
print(max(mat.values()))
