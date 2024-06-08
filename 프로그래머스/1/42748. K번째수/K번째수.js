function solution(array, commands) {
    var answer = [];
    for (const [i, j, k] of commands) {
        const sliced_array = array.slice(i-1, j).sort((a, b) => a - b);
        answer.push(sliced_array[k-1]);
    }
    return answer;
}