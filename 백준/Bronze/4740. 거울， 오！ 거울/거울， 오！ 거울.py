import sys
while True:
    n = sys.stdin.readline().rstrip('\n')
    if n == "***":
        break
    n = n[::-1]
    print(n)
