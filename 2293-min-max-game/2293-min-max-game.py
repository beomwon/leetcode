class Solution:
    def minMaxGame(self, nums):
        while True:
            if len(nums) == 1: return nums[0]
            temp = []
            flag=True
            for i in range(0,len(nums),2):
                if flag:
                    temp.append(min(nums[i],nums[i+1]))
                    flag=False
                else:
                    temp.append(max(nums[i],nums[i+1]))
                    flag=True
            nums = temp