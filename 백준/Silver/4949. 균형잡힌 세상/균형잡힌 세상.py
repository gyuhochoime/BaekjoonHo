import sys
from collections import deque
while True:
    n = sys.stdin.readline().rstrip()
    if n == ".":
        break
    ho = deque()
    for i in n:
        if i in "([":
            ho.append(i)
        elif i == ")":
            if ho and ho[-1] == "(":
                ho.pop()
            else:
                ho.append(i)
                break
        elif i == "]":
            if ho and ho[-1] == "[":
                ho.pop()
            else:
                ho.append(i)
                break
    if ho:
        print("no")
    else:
        print("yes")
