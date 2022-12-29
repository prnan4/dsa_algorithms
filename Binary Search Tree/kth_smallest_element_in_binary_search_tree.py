# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallestPreOrder(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        nums = []
        def treeTraversal(root, nums):
            nums.append(root.val)
            if root.left: treeTraversal(root.left, nums)
            if root.right: treeTraversal(root.right, nums)
        
        treeTraversal(root, nums)
        nums.sort()
        return nums[k-1]

    def kthSmallestInOrder(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        nums = []
        def treeTraversal(root, nums):
            if root.left: treeTraversal(root.left, nums)
            nums.append(root.val)
            if root.right: treeTraversal(root.right, nums)
        
        treeTraversal(root, nums)
        return nums[k-1]
        