def solution(phone_number):
    answer = "*" * (len(phone_number) - 4)
    for i in range(len(phone_number) - 4, len(phone_number)):
        answer += phone_number[i]
    return answer