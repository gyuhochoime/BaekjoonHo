def solution(myString):
    a = 0
    answer = []
    for i in range(len(myString)):
        if myString[i] == "x":
            answer.append(a)
            a = 0
        else:
            a += 1
    answer.append(a)
    return answer