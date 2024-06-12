function solution(numbers, target) {
    let answer = 0;
    const dfs = (currentValue, count) => {
        if (count === numbers.length) {
            if (currentValue === target) {answer += 1; };
            return;
        }
        dfs(currentValue + numbers[count], count+1);
        dfs(currentValue - numbers[count], count+1);
    }
    dfs(0, 0);
    return answer;
}