import sys
w = []
k = []
wt = 0
kt = 0
first = []
for i in range(10):
    n = int(sys.stdin.readline().rstrip())
    w.append(n)
for i in range(10):
    m = int(sys.stdin.readline().rstrip())
    k.append(m)
w.sort(reverse = True)
k.sort(reverse = True)
for i in range(3):
    wt += w[i]
for i in range(3):
    kt += k[i]
first.append(wt)
first.append(kt)
for i in first:
    print(i, end = " ")
