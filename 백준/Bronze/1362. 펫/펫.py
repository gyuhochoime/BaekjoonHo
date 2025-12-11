import sys
happy = ":-)"
sad = ":-("
die = "RIP"
num = 1
while True:
    n, m = map(int, sys.stdin.readline().rstrip().split())
    if n == 0 and m == 0:
        break
    dead = False
    while True:
        a, b = map(str, sys.stdin.readline().rstrip().split())
        if a == "F":
            if not dead:
                m += int(b)
        elif a == "E":
            if not dead:
                m -= int(b)
                if m <= 0:
                    dead = True
        elif a == "#" and b == "0":
            if dead or m <= 0:
                print("%d %s" % (num, die))
            elif m > (n // 2) and m < (n * 2):
                print("%d %s" % (num, happy))
            else:
                print("%d %s" % (num, sad))
            break
    num += 1
