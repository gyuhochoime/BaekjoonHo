import sys
n = int(sys.stdin.readline())
a = sys.stdin.readline().rstrip()
two = 0
e = 0
for i in a:
    if i == "2":
        two += 1
    else:
        e += 1
if two > e:
    print(2)
elif two < e:
    print("e")
else:
    print("yee")
