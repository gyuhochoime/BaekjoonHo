def solution(num_list):
    tot_1 = 1
    tot_2 = 0
    answer = 0
    for i in num_list:
        tot_1 *= i
        tot_2 += i
    tot_2 **= 2
    if tot_1 < tot_2:
        answer = 1
    return answer