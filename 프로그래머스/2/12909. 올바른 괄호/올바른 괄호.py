def solution(s):
    s = list(s)
    stack = []
    lt = 0
    rt = 0
    for i in s:
        if i == "(":
            lt += 1
        elif i == ")":
            rt += 1
    if lt != rt:
        return False
    for i in s:
        if i == ")":
            if not stack:
                return False
            else:
                stack.pop()
        if i == "(":
            stack.append(i)
    else:
        return True