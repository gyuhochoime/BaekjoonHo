def solution(arr, n):
    answer = []
    tmp = len(arr)
    if tmp % 2 == 0:
        for i in range(tmp):
            if i % 2 == 1:
                answer.append(arr[i] + n)
            elif i % 2 == 0:
                answer.append(arr[i])
    elif tmp % 2 == 1:
        for i in range(tmp):
            if i % 2 == 0:
                answer.append(arr[i] + n)
            elif i % 2 == 1:
                answer.append(arr[i])
    return answer