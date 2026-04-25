function solution(n) {
    let answer = Math.floor(n / 7)
    if (n / 7 != answer)
        answer += 1
    return answer
}