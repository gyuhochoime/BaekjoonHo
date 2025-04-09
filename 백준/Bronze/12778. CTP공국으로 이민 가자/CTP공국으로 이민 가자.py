import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    n, m = map(str, sys.stdin.readline().rstrip().split())
    arr = list(map(str, sys.stdin.readline().rstrip().split()))
    n = int(n)
    for j in range(n):
        if m == "C":
            arr[j] = ord(arr[j]) - 64
        elif m =="N":
            arr[j] = chr(int(arr[j])+64)
    for s in arr:
        print(s, end = " ")
    print()
            
