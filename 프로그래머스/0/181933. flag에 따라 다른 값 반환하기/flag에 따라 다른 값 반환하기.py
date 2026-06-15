def solution(a, b, flag):
    answer = 0
    if flag:
        answer = a + b
    if not flag:
        answer = a - b
    return answer