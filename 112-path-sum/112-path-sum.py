# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root, targetSum) -> bool:
        global res
        if root == None: return False
        
        res = False

        def search(node, sum_, target):
            global res
            sum_ += node.val
            if node.left == None and node.right == None:
                if sum_ == target: res = True
                return
            if node.left: search(node.left, sum_, target)
            if node.right: search(node.right, sum_, target)
        
        search(root, 0, targetSum)
        return res