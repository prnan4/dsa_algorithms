# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def findHeight(self, root):
        if not root: return -1
        return max(self.findHeight(root.left) + 1, self.findHeight(root.right) + 1)
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        
        return abs(self.findHeight(root.left) - self.findHeight(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
        