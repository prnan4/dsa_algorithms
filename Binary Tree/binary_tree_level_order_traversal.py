# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderRecursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root: return result
        
        def dfs(node, level):
            if not node: return
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            return result
            
        return dfs(root, 0)

    def levelOrderIterativeUsingQueue(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root: return result
        
        queue = [root]
        while queue:
            levelnodes = []
            qlen = len(queue)
            
            for i in range(qlen):
                root = queue.pop(0)
                levelnodes.append(root.val)
                if root.left: queue.append(root.left)
                if root.right: queue.append(root.right)
    
            result.append(levelnodes)
        return result