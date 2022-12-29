# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    max_path = 0
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def height(root):
            if root is None:
                return -1
            return max(height(root.left), height(root.right)) + 1
        
        def findDiameter(root):
            if root is None:
                return
            len_l = height(root.left) + 1
            len_r = height(root.right) + 1
            self.max_path = max(self.max_path, len_l + len_r)
            
            findDiameter(root.left)
            findDiameter(root.right)
            
        findDiameter(root)
        return self.max_path