def solution(arr):
    answer = [arr[0]]
    stack = arr[0]
    for i in range(1, len(arr)):
        if arr[i] == stack:
            continue
        else:
            answer.append(arr[i])
            stack = arr[i]
    return answer