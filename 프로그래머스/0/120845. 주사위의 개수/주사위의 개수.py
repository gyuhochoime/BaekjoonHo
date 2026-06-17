def solution(box, n):
    answer = 1
    for i in box:
        if i // n >= 1:
            answer *= i // n
        else:
            answer = 0
            break
    return answer