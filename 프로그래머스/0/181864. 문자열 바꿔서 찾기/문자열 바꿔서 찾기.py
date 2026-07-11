def solution(myString, pat):
    answer = 0
    tmp = list(myString)
    moonjayul = ""
    for i in tmp:
        if i == "A":
            moonjayul += "B"
        elif i == "B":
            moonjayul += "A"
    if pat in moonjayul:
        answer = 1
    return answer