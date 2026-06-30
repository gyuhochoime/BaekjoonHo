def solution(my_string, n):
    tmp = len(my_string) - n
    answer = my_string[tmp:]
    return answer