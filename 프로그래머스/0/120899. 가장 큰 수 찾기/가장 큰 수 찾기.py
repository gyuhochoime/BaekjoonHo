def solution(array):
    answer = []
    a = b = -1
    for i in range(len(array)):
        if array[i] > a:
            a = array[i]
            b = i
    answer.append(a)
    answer.append(b)
    return answer