function solution(n) {
    let even = 0
    for (let i = 1; i < n + 1; i++) {
        if (i % 2 === 0) {
            even += i
        }
    }
    return even
}