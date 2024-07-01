function solution(people, limit) {
    people = people.sort((x, y)=>y-x);
    let count = 0;
    
    const saved_people = Array(people.length).fill(false);
    
    let compare_idx = people.length-1;
    
    for (let i = 0; i < people.length; i++) {
        if (saved_people[i]) continue;
        if (compare_idx > 0 && people[i] + people[compare_idx] <= limit) {
            saved_people[compare_idx] = true;
            compare_idx--;
        }
        saved_people[i] = true;
        count++;
    }
    
    return count;
}