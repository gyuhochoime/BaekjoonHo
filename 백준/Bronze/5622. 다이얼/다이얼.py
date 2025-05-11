import sys
n = list(sys.stdin.readline().rstrip())
a = ["A", "B", "C"]
b = ["D", "E", "F"]
c = ["G", "H", "I"]
d = ["J", "K", "L"]
e = ["M", "N", "O"]
f = ["P", "Q", "R", "S"]
g = ["T", "U", "V"]
h = ["W", "X", "Y", "Z"]
tot = 0
for i in n:
    if i in a:
        tot += 3
    elif i in b:
        tot += 4
    elif i in c:
        tot += 5
    elif i in d:
        tot += 6
    elif i in e:
        tot += 7
    elif i in f:
        tot += 8
    elif i in g:
        tot += 9
    elif i in h:
        tot += 10
print(tot)
