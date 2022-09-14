# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        global max_
        max_ = 0
        def goBottom(node, level):
            global max_
            if not node: return
            level += 1
            if level > max_: max_ = level
            if node.left: goBottom(node.left, level)
            if node.right: goBottom(node.right, level)
        goBottom(root, 0)
        return max_
            