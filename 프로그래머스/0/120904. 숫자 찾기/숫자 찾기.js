function solution(num, k) {
    const a = String(num)
    let answer = -1
    for (let i = 1; i <= a.length; i++) {
        if (a[i-1] === String(k)) {
            answer = i
            break
        }
    }
    return answer
}