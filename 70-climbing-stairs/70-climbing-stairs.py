class Solution:
    def climbStairs(self, n):
        if n < 4: return n
        dummy = [1, 2, 3, 5]
        for i in range(4, n):
            dummy.append(dummy[i-1]+dummy[i-2])
        return dummy[-1]