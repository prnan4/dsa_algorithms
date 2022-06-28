# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        curr = root
        
        def invert(curr):
            if not curr: return
            temp = curr.left
            curr.left = curr.right
            curr.right = temp 
            invert(curr.left)
            invert(curr.right)
        invert(curr)
        return curr