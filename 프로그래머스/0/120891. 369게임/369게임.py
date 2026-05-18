def solution(order):
    tmp = str(order)
    answer = 0
    for i in range(len(tmp)):
        if tmp[i] in ["3", "6", "9"]:
            answer += 1
    return answer