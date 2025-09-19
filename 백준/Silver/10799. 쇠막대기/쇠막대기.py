import sys
n = sys.stdin.readline().rstrip()
stack = []
tot = 0
for i in range(len(n)):
    if n[i] == "(":
        stack.append(n[i])
    else:
        if n[i-1] == "(":
            stack.pop()
            tot += len(stack)
        else:
            stack.pop()
            tot += 1
print(tot)
