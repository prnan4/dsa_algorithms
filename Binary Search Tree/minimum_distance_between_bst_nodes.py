# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodes = []
        def inorder(node):
            if node is not None:
                if node.left: inorder(node.left)
                nodes.append(node.val)
                if node.right: inorder(node.right)
        inorder(root)
        min_diff = float('inf')
        for i in range(0, len(nodes) -1):
            diff = nodes[i+1] - nodes[i]
            if diff < min_diff:
                min_diff = diff
        return min_diff