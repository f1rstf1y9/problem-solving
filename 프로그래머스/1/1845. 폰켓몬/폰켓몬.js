function solution(nums) {
    let poketmon_counts = nums.length;
    let nums_set = [];
    for (let i = 0; i < poketmon_counts; i++) {
        if (!nums_set.includes(nums[i])){
            nums_set.push(nums[i]);
        }
    }
    let set_length = nums_set.length;
    return set_length < poketmon_counts / 2 ? set_length : poketmon_counts / 2;
}