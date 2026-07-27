def solution(myString):
    answer = ''
    arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
    for i in range(len(myString)):
        if myString[i] in arr:
            answer += "l"
        else:
            answer += myString[i]
    return answer