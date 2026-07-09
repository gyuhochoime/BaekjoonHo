def solution(my_string, num1, num2):
    answer = ''
    a = my_string[num1]
    b = my_string[num2]
    c = list(my_string)
    c[num1] = b
    c[num2] = a
    for i in c:
        answer += i
    return answer