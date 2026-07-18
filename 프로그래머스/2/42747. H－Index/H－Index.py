def solution(citations):
    arr = sorted(citations, reverse = True)
    cnt = 0
    for i in range(len(arr)):
        if cnt +1 <= arr[i]:
            cnt += 1
        else:
            break
    return cnt