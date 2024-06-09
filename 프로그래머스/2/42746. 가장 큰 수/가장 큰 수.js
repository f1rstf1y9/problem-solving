function solution(numbers) {
    const sorted_numbers = numbers.sort((a, b)=>{
        a = String(a);
        b = String(b);
        return (b+a) - (a+b);
    }).join("")
    return sorted_numbers[0] === "0" ? "0" : sorted_numbers;
}