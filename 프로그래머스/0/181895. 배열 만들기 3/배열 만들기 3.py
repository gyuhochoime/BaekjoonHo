def solution(arr, intervals):
    answer = []
    for key, value in intervals:
        tmp = arr[key:value+1]
        for i in tmp:
            answer.append(i)
    return answer