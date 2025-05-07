import sys
burger = []
beverage = []
for i in range(3):
    n = int(sys.stdin.readline().rstrip())
    burger.append(n)
for i in range(2):
    m = int(sys.stdin.readline().rstrip())
    beverage.append(m)
print(min(burger) + min(beverage) - 50)
