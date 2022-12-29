# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        root_val = preorder.pop(0)
        root = TreeNode(root_val)

        root_index_inorder = inorder.index(root_val)

        if len(inorder) == 1: return TreeNode(inorder[0])

        if root_index_inorder == 0:
            # Only right subtree exists
            root.right = self.buildTree(preorder, inorder[1:])

        elif root_index_inorder == len(inorder) - 1:
            # Only left subtree exists
            root.left = self.buildTree(preorder, inorder[:-1])

        else:
            #Both subtrees exists
            root.left = self.buildTree(preorder, inorder[:root_index_inorder])
            root.right = self.buildTree(preorder, inorder[root_index_inorder+1:])

        return root
                
        