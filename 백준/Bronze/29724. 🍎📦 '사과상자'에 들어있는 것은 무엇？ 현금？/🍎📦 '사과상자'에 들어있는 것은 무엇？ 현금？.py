import sys
T = int(sys.stdin.readline().rstrip())
applePay = 0
jilrang = 0
for i in range(T):
    n, m, k, r = map(str, sys.stdin.readline().rstrip().split())
    apple = (int(m) // 12) * (int(k) // 12) * (int(r) // 12)
    if n == "A":
        applePay += apple * 4000
        jilrang += 1000 + apple * 500
    elif n == "B":
        jilrang += 6000
print(jilrang)
print(applePay)
