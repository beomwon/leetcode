# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        curLv, res = [root], []
        
        while len(curLv):
            sum_ = 0
            temp = curLv
            curLv = []
            for v in temp:
                sum_ += v.val
                if v.left:
                    curLv.append(v.left)
                if v.right:
                    curLv.append(v.right)
                    
            res.append(sum_/len(temp))
        
        return res
            
            