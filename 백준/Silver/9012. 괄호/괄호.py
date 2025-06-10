import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    left = 0
    right = 0
    n = list(sys.stdin.readline().rstrip())
    for i in n:
        if i == "(":
            left += 1
        elif i == ")":
            right += 1
            if right > left:
                break
    if left == right and n[0] == "(" and n[len(n)-1] == ")":
        print("YES")
    else:
        print("NO")
        
