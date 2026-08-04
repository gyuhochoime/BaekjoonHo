def solution(my_string, is_suffix):
    answer = 0
    a = len(is_suffix)
    if my_string[len(my_string)-a:] == is_suffix:
        answer = 1
    return answer