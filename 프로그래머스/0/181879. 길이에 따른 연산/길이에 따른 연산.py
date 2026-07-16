def solution(num_list):
    n = len(num_list)
    if n >= 11:
        return sum(num_list)
    else:
        a = 1
        for i in num_list:
            a *= i
        return a