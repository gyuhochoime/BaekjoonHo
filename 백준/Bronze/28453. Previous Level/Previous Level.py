import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
for i in arr:
    if i < 250:
        print("4", end = " ")
    elif i >= 250 and i < 275:
        print("3", end = " ")
    elif i >= 275 and i < 300:
        print("2", end = " ")
    elif i == 300:
        print("1", end = " ")
