function solution(n) {
    const a = String(n)
    let answer = 0
    for (let i = 0; i < a.length; i++) {
        answer += Number(a[i])
    }
    return answer
}