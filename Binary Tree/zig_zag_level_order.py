# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = deque()
        direction = 1
        res = []
        if root: 
            queue.append(root)
        
        while queue:
            level = []
            for i in range(0, len(queue)):
                root = queue.popleft()
                level.append(root.val)
                if root.left: queue.append(root.left)
                if root.right: queue.append(root.right)
            res.append(level[::direction])
            direction *= -1
        return res