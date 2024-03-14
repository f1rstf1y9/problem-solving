class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked_nums = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in checked_nums:
                return [checked_nums[diff], i]
            else:
                checked_nums[nums[i]] = i