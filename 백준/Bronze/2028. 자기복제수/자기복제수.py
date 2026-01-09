import sys
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    a = int(sys.stdin.readline().rstrip())
    ren = len(str(a))
    ja = str(a ** 2)
    if ja[-ren:] == str(a):
        print("YES")
    else:
        print("NO")
