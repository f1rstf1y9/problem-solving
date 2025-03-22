const fs = require('fs');
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [N, M] = input[0].split(" ").map(Number);;
const guitars = Array.from({length: N}, () => 0n);

for (let i = 0; i < N; i++) {
    const valiableSongs = input[i+1].split(" ")[1].replaceAll('Y', '1').replaceAll('N', '0');
    guitars[i] = BigInt('0b' + valiableSongs);
}

let maxValue = 0n;
let maxCount = 0;

const backtracking = (currentValue, currentIdx, currentCount) => {
    if (currentValue === maxValue) {
        maxCount = Math.min(maxCount, currentCount);
    }
    if (currentValue > maxValue) {
        maxValue = currentValue;
        maxCount = currentCount;
    }
    
    if (currentIdx === N) return;
    
    backtracking(currentValue | guitars[currentIdx], currentIdx+1, currentCount+1);
    backtracking(currentValue, currentIdx+1, currentCount);
    
}

backtracking(0n, 0, 0);

console.log((maxValue ? maxCount : -1))