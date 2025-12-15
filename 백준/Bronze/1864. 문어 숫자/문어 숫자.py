import sys
while True:
    n = sys.stdin.readline().rstrip()
    if n == "#":
        break
    moon = len(n)
    tot = 0
    for i in n:
        if i == "-":
            tot += 0
        elif i == "\\":
            tot += 1 * (8 ** (moon - 1))
        elif i == "(":
            tot += 2 * (8 ** (moon - 1))
        elif i == "@":
            tot += 3 * (8 ** (moon - 1))
        elif i == "?":
            tot += 4 * (8 ** (moon - 1))
        elif i == ">":
            tot += 5 * (8 ** (moon - 1))
        elif i == "&":
            tot += 6 * (8 ** (moon - 1))
        elif i == "%":
            tot += 7 * (8 ** (moon - 1))
        elif i == "/":
            tot += -1 * (8 ** (moon - 1))
        moon -= 1
    print(tot)
