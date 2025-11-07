import sys
n = int(sys.stdin.readline().rstrip())
dal = 0
po = 0
for _ in range(n):
    a = sys.stdin.readline().rstrip()
    if abs(dal - po) < 2:
        if a == "D":
            dal += 1
        elif a == "P":
            po += 1
print("%d:%d" % (dal, po))
