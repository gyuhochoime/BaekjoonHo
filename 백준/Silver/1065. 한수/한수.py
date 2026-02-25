import sys
n = int(sys.stdin.readline())
if n < 100:
    print(n)
else:
    tot = 99
    for i in range(100, n + 1):
        a = str(i)
        dc = int(a[1]) - int(a[0])
        for j in range(len(a) - 1):
            if int(a[j+1]) - int(a[j]) != dc:
                break
        else:
            tot += 1
    print(tot)
