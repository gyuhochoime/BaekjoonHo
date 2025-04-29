import sys
n = list(map(str, sys.stdin.readline().rstrip()))
front = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
back = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
for i in range(len(n)):
    if n[i] in front:
        n[i] = chr(ord(n[i]) + 13)
    elif n[i] in back:
        n[i] = chr(ord(n[i]) - 13)
for i in n:
    print(i, end = "")
