import sys
while True:
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    if a[0] == 0 and a[1] == 0 and a[2] == 0:
        break
    a.sort()
    if a[2] >= a[0] + a[1]:
             print("Invalid")
    else:
        if a[0] == a[1] and a[1] == a[2]:
            print("Equilateral")
        elif a[0] != a[1] and a[1] != a[2] and a[2] != a[0]:
            print("Scalene")
        else:
            print("Isosceles")
