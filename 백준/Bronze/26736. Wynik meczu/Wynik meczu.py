import sys
arr = list(map(str, sys.stdin.readline().rstrip()))
cna = 0
cnb = 0
for i in arr:
    if i == "A":
        cna += 1
    else:
        cnb += 1
print("%d : %d" % (cna, cnb))
