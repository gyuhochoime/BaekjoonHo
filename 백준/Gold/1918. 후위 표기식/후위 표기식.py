import sys
arr = sys.stdin.readline().rstrip()
postfix = ""
stack = []
for i in arr:
    if i.isalpha():
        postfix += i
    else:
        if i == "(":
            stack.append(i)
        elif i == "*" or i == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                postfix += stack.pop()
            stack.append(i)
        elif i == "+" or i == "-":
            while stack and stack[-1] != "(":
                postfix += stack.pop()
            stack.append(i)
        elif i == ")":
            while stack and stack[-1] != "(":
                postfix += stack.pop()
            stack.pop()
while stack:
    postfix += stack.pop()
print(postfix)
