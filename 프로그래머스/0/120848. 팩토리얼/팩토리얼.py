def solution(n):
    if n >= 3628800:
        return 10
    elif n >= 362880:
        return 9
    elif n >= 40320:
        return 8
    elif n >= 5040:
        return 7
    elif n >= 720:
        return 6
    elif n >= 120:
        return 5
    elif n >= 24:
        return 4
    elif n >= 6:
        return 3
    elif n >= 2:
        return 2
    else:
        return 1