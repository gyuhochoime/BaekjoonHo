from collections import deque
def solution(rny_string):
    answer = deque(rny_string)
    tmp = ""
    n = len(answer)
    for _ in range(n):
        a = answer.popleft()
        if a == "m":
            answer.append("r")
            answer.append("n")
        else:
            answer.append(a)
    answer = list(answer)
    for i in answer:
        tmp += i
    return tmp