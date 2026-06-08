def solution(array):
    cnt = 0
    for i in array:
        for j in range(len(str(i))):
            if str(i)[j] == "7":
                cnt += 1
    return cnt