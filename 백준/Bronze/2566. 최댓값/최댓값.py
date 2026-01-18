import sys
n = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(9)]
mex = 0
heng = 0
yul = 0
for i in range(9):
    for j in range(9):
        if n[i][j] >= mex:
            mex = n[i][j]
            heng = i + 1
            yul = j + 1
print(mex)
print(heng, yul)
