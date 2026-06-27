def solution(arr1, arr2):
    answer = 0
    a = len(arr1)
    b = len(arr2)
    c = sum(arr1)
    d = sum(arr2)
    if a > b:
        answer = 1
    elif a == b:
        if c > d:
            answer = 1
        elif c == d:
            answer = 0
        elif c < d:
            answer = -1
    elif a < b:
        answer = -1
    return answer