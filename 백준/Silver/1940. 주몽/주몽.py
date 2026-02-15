import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
armor = list(map(int, sys.stdin.readline().split()))
armor.sort()
lt = 0
rt = n - 1
su = 0
while lt < rt:
    s = armor[lt] + armor[rt]
    if s == m:
        su += 1
        lt += 1
        rt -= 1
    elif s < m:
        lt += 1
    else:
        rt -= 1
print(su)
