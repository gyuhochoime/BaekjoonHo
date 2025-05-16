import sys
tot = 0
grade = 0
for i in range(20):
    n, m, k = map(str, sys.stdin.readline().rstrip().split())
    if k == "A+":
        tot += float(m) * 4.5
        grade += float(m)
    elif k == "A0":
        tot += float(m) * 4.0
        grade += float(m)
    elif k == "B+":
        tot += float(m) * 3.5
        grade += float(m)
    elif k == "B0":
        tot += float(m) * 3.0
        grade += float(m)
    elif k == "C+":
        tot += float(m) * 2.5
        grade += float(m)
    elif k == "C0":
        tot += float(m) * 2.0
        grade += float(m)
    elif k == "D+":
        tot += float(m) * 1.5
        grade += float(m)
    elif k == "D0":
        tot += float(m) * 1.0
        grade += float(m)
    elif k == "F":
        tot += 0
        grade += float(m)
    else:
        tot += 0
hakjum = tot / grade
print("%.6f" % hakjum)
