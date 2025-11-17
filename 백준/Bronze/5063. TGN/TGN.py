import sys
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    r, e, c = map(int, sys.stdin.readline().rstrip().split())
    adn = e - c
    if r > adn:
        print("do not advertise")
    elif r == adn:
        print("does not matter")
    else:
        print("advertise")
