import sys
n = list(sys.stdin.readline().rstrip())
m = []
for i in range(len(n)):
    if n[i] == "x" and i != 0:
        m = n[:i]
        break
    elif n[i] == "x" and i == 0:
        m.append(1)
        break
    elif n[i] == "-" and n[i+1] == "x":
        m.append(-1)
        break
if m == []:
    print(0)
for i in m:
    print(i, end = "")
