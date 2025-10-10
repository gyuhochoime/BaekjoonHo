import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    n, m = map(str, sys.stdin.readline().rstrip().split())
    m = int(m)
    if m <= 100 and m >= 97:
        print(n, "A+")
    elif m <= 96 and m >= 90:
        print(n, "A")
    elif m <= 89 and m >= 87:
        print(n, "B+")
    elif m <= 86 and m >= 80:
        print(n, "B")
    elif m <= 79 and m >= 77:
        print(n, "C+")
    elif m <= 76 and m >= 70:
        print(n, "C")
    elif m <= 69 and m >= 67:
        print(n, "D+")
    elif m <= 66 and m >= 60:
        print(n, "D")
    else:
        print(n, "F")
