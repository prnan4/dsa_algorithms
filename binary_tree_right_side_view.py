# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = [root]
        res = []
        
        if not root: return []
        while queue:
            res.append(queue[-1].val)
            qlen = len(queue)
            for i in range(qlen):
                root = queue.pop(0)
                if root.left: queue.append(root.left)
                if root.right: queue.append(root.right)
        return res
                       