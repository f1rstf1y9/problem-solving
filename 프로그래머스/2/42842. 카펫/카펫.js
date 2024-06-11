function solution(brown, yellow) {
    for (let i = 0; i <= yellow; i++) {
        if (yellow % i === 0) {
            const row = yellow/i;
            const column = i;
            if(row*2 + column*2 + 4 === brown) {
                return [row+2, column+2];
            }
        }
    }
}