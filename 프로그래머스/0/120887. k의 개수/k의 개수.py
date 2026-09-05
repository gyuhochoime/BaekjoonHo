def solution(i, j, k):
    answer = 0
    for i in range(i, j + 1):
        a = str(i)
        for n in range(len(a)):
            if int(a[n]) == k:
                answer += 1
    return answer