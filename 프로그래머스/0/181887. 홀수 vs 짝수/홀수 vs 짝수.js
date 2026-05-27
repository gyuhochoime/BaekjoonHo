function solution(num_list) {
    let answer = 0
    let odd = 0
    let even = 0
    for (let i = 1; i <= num_list.length; i++)
        {
            if (i % 2 == 1) {
                even += num_list[i-1]
            } else if (i % 2 == 0) {
                odd += num_list[i-1]
            }
        }
    answer = Math.max(odd, even)
    return answer
}