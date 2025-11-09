import sys
n = int(sys.stdin.readline().rstrip())
one = 0
two = 0
three = 0
four = 0
axis = 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a == 0 or b == 0:
        axis += 1
    else:
        if a > 0 and b > 0:
            one += 1
        elif a < 0 and b > 0:
            two += 1
        elif a < 0 and b < 0:
            three += 1
        elif a > 0 and b < 0:
            four += 1
print("Q1: %d" % one)
print("Q2: %d" % two)
print("Q3: %d" % three)
print("Q4: %d" % four)
print("AXIS: %d" % axis)
