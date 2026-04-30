function solution(n, k) {
    let sale = 0
    sale += 12000 * n + 2000 * (k - Math.floor(n / 10))
    return sale
}