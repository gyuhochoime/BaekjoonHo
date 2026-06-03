def solution(n):
    a = str(n)
    answer = 0
    for i in range(len(a)):
        answer += int(a[i])
    return answer