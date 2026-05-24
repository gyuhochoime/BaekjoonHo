import math
def solution(n):
    answer = 0
    tmp = math.sqrt(n)
    if tmp.is_integer():
        answer = 1
    else:
        answer = 2
    return answer