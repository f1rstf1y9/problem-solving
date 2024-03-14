class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = list(sorted([(i,nums[i]) for i in range(len(nums))],key=lambda x:x[1]))
        l, r = 0, len(nums)-1
        while l < r:
            if nums_dict[l][1]+nums_dict[r][1] > target:
                r -= 1
            elif nums_dict[l][1]+nums_dict[r][1] < target:
                l += 1
            else:
                return list(sorted([nums_dict[l][0],nums_dict[r][0]]))