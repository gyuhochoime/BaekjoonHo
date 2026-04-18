def solution(s):
    answer = ""
    arr = list(s)
    arr.sort(reverse = True)
    for i in arr:
        answer += i
    return answer