import sys
n = list(sys.stdin.readline().rstrip())
for i in range(len(n)):
    if n[i] == "E":
        n[i] = "I"
    elif n[i] == "I":
        n[i] = "E"
    elif n[i] == "S":
        n[i] = "N"
    elif n[i] == "N":
        n[i] = "S"
    elif n[i] == "F":
        n[i] = "T"
    elif n[i] == "T":
        n[i] = "F"
    elif n[i] == "P":
        n[i] = "J"
    elif n[i] == "J":
        n[i] = "P"
for i in n:
    print(i, end = "")
