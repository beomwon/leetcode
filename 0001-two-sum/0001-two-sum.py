class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            try:
                j = nums.index(target - nums[i])
                if i != j:
                    return [i, j]
            except:
                continue
