function solution(slice, n) {
    let answer = Math.floor(n / slice)
    if (n / slice !== answer)
        answer += 1
    return answer
}