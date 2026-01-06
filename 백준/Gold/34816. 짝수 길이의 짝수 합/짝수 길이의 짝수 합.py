import sys
n, q = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip()))
for _ in range(q):
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    if a[0] == 1:
        if arr[a[1]-1] == 1:
            arr[a[1]-1] = 0
        else:
            arr[a[1]-1] = 1
    elif a[0] == 2:
        if a[2] - a[1] >= 3:
            print("YES")
        elif a[2] - a[1] == 2:
            if arr[a[1]-1:a[2]] == [1, 0, 1] or arr[a[1]-1:a[2]] == [0, 1, 0]:
                print("NO")
            else:
                print("YES")
        elif a[2] - a[1] == 1:
            if arr[a[1]-1:a[2]] == [1, 0] or arr[a[1]-1:a[2]] == [0, 1]:
                print("NO")
            else:
                print("YES")
        else:
            print("NO")
