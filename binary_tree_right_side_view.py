# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideViewIterativeUsingQueue(self, root):
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

    def rightSideViewRecursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        levelorder = []
        if not root: return result
        
        def dfs(root, level):
            if not root: return
            if len(levelorder) == level:
                levelorder .append([])
            levelorder[level].append(root.val)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        
        dfs(root, 0)
        
        result = []
        for level in levelorder:
            result.append(level[-1])
        
        return result
                       