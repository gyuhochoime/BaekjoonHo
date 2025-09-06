import sys
n = int(sys.stdin.readline().rstrip())
arr = []
tot = 0
for i in range(n):
    a = sys.stdin.readline().rstrip()
    arr.append(a)
for i in arr:
    if i == "Poblano":
        tot += 1500
    elif i == "Mirasol":
        tot += 6000
    elif i == "Serrano":
        tot += 15500
    elif i == "Cayenne":
        tot += 40000
    elif i == "Thai":
        tot += 75000
    elif i == "Habanero":
        tot += 125000
print(tot)
