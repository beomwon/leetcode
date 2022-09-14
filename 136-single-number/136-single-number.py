class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        while True:
            try:
                target = nums[0]
                nums.remove(target)
                nums.remove(target)
            except:
                return target