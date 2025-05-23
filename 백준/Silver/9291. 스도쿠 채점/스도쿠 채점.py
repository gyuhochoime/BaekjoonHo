import sys

def sudoku(a):
    for i in range(9):
        tst1 = [0] * 10
        tst2 = [0] * 10
        for j in range(9):
            tst1[a[i][j]] = 1
            tst2[a[j][i]] = 1
        if sum(tst1) != 9 or sum(tst2) != 9:
            return False
    for i in range(3):
        for j in range(3):
            tst3 = [0] * 10
            for k in range(3):
                for s in range(3):
                    tst3[a[i*3+k][j*3+s]] = 1
            if sum(tst3) != 9:
                return False
    return True

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(9)]
    
    if i != T - 1:
        sys.stdin.readline()
    
    if sudoku(arr):
        print("Case %d: CORRECT" % (i + 1))
    else:
        print("Case %d: INCORRECT" % (i + 1))
