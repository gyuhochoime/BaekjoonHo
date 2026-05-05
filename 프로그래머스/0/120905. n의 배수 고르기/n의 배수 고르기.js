function solution(n, numlist) {
    let answer = numlist.filter(v => v % n === 0)
    return answer
}