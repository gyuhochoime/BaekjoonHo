def solution(sizes):
    answer = 0
    mini = maxi = 0
    for garo, sero in sizes:
        tmp_mini = min(garo, sero)
        tmp_maxi = max(garo, sero)
        if tmp_mini > mini:
            mini = tmp_mini
        if tmp_maxi > maxi:
            maxi = tmp_maxi
    return mini * maxi