def solution(s):
    answer = ''
    arr = list(map(int, s.split()))
    a = min(arr)
    b = max(arr)
    answer += str(a)
    answer += " "
    answer += str(b)
    return answer