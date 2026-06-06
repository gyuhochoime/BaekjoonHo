import math
def solution(n):
    answer = 0
    a = math.sqrt(n)
    if a == int(a):
        answer = (a + 1) ** 2
    else:
        answer = -1
    return answer