class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        try:
            return nums[-3]
        except:
            return nums[-1]