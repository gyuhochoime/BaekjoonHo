function solution(my_string, n) {
    let answer = ''
    const arr = [...my_string]
    for (let i = 0; i < arr.length; i++)
        {
            answer += arr[i].repeat(n)
        }
    return answer
}