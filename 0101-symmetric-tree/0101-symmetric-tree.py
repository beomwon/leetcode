# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        global leftLst, rightLst

        left = root.left
        right = root.right
        
        leftLst = []
        rightLst = []
        
        def leftTraversal(node):
            global leftLst
            leftLst.append(node.val)
            
            if node.left: leftTraversal(node.left)
            else: leftLst.append('.')
                
            if node.right: leftTraversal(node.right)
            else: leftLst.append('.')
        
        def rightTraversal(node):
            global rightLst
            rightLst.append(node.val)
            
            if node.right: rightTraversal(node.right)
            else: rightLst.append('.')
                
            if node.left: rightTraversal(node.left)
            else: rightLst.append('.')
            
        if left != None: leftTraversal(left) 
        if right != None: rightTraversal(right) 
        
        print(leftLst)
        print(rightLst)
        return leftLst == rightLst
            
        
