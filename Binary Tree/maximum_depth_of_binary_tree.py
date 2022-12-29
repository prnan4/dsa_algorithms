# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        maxDepth = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        return maxDepth

    def maxDepthUsingStack(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        maxDepth = 0
        stack.append((1, root))
        
        while stack:
            currDepth, root = stack.pop()
            if root:
                maxDepth = max(currDepth, maxDepth)
                stack.append((currDepth + 1, root.left))
                stack.append((currDepth + 1, root.right))
                
        return maxDepth