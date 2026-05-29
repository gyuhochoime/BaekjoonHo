def solution(n):
    arr = list(str(n))
    arr.sort(reverse = True)
    ans = ""
    for i in arr:
        ans += i
    ans = int(ans)
    return ans