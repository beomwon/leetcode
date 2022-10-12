class Solution:
    def largestPerimeter(self, nums):
        nums = sorted(nums, reverse=False)
        max_ = 0
        for i in range(len(nums[:-2])):
            if nums[i] + nums[i+1] > nums[i+2] and max_ < sum(nums[i:i+3]):
                max_ = sum(nums[i:i+3])
                
        return max_