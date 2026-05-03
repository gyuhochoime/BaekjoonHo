function solution(numbers) {
    let answer = [...numbers].sort((a, b) => a - b)
    let tot = 0
    const len = numbers.length
    tot += answer[len-1] * answer[len-2]
    return tot
}