import sys
while True:
    n = sys.stdin.readline().rstrip()
    arr = []
    if n == "END":
        break
    for i in n[::-1]:
        arr.append(i)
    for i in arr:
        print(i, end = '')
    print()
