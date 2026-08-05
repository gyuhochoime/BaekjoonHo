def solution(my_string, is_prefix):
    answer = 0
    a = len(is_prefix)
    if is_prefix == my_string[:a]:
        answer = 1
    return answer