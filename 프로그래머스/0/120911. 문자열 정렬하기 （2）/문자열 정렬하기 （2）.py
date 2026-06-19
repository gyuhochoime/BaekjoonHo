def solution(my_string):
    answer = my_string.lower()
    answer = list(answer)
    answer.sort()
    ans = ""
    for i in answer:
        ans += i
    return ans