import sys
n = int(sys.stdin.readline().rstrip())
pibo = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
for _ in range(40):
    pibo.append(pibo[-1] + pibo[-2])
print(pibo[n])
