# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, node):
        
        if not node:
            return ''
        
        left = '(%s)' % self.tree2str(node.left) if (node.left or  node.right) else ''
        right = '(%s)' % self.tree2str(node.right) if node.right else ''
        return '%d%s%s' % (node.val, left, right)
