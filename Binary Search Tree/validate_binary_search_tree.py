# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def validate(root, low=-float('inf'), high=float('inf')):
            if not root: return True
            if not root.val > low or not root.val < high: return False
            if validate(root.left, low, root.val) and validate(root.right, root.val, high): return True
            
        return validate(root)
        
                