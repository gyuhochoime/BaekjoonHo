import sys
n = sys.stdin.readline().rstrip()
tot = 0
a = 1
su = 0
for i in n:
    if i.isdigit():
        tot += a * int(i)
    else:
        su = a
    if a == 1:
        a = 3
    else:
        a = 1
if su == 1:
    na = tot % 10
    print(10 - na)
else:
    na = tot % 10
    if na == 1:
        print(3)
    elif na == 2:
        print(6)
    elif na == 3:
        print(9)
    elif na == 4:
        print(2)
    elif na == 5:
        print(5)
    elif na == 6:
        print(8)
    elif na == 7:
        print(1)
    elif na == 8:
        print(4)
    elif na == 9:
        print(7)
    elif na == 0:
        print(0)
