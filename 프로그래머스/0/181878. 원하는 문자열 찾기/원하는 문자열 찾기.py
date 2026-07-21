def solution(myString, pat):
    answer = 0
    a = myString.lower()
    b = pat.lower()
    if b in a:
        answer = 1
    return answer