import sys
n = int(sys.stdin.readline().rstrip())
su = 2
while n > 1:
    if n % su == 0:
        n //= su
        print(su)
    else:
        su += 1
