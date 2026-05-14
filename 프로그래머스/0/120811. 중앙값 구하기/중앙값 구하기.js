function solution(array) {
    let arr = [...array].sort((a, b) => a - b)
    const a = Math.floor(array.length / 2)
    return arr[a]
}