import sys
for _ in range(3):
    arr = list(map(int, sys.stdin.readline().split()))
    a = b = 0
    for i in arr:
        if i == 0:
            a += 1
        elif i == 1:
            b += 1
    if a == 0:
        print("E")
    elif a == 1:
        print("A")
    elif a == 2:
        print("B")
    elif a == 3:
        print("C")
    elif a == 4:
        print("D")