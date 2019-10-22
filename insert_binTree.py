
# Given the root node of a binary search tree (BST) and a value to be inserted into the tree, 
# insert the value into the BST. Return the root node of the BST after the insertion. 
# It is guaranteed that the new value does not exist in the original BST.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        if root == None:
            root = TreeNode(val)
            return root
        
        if val > root.val:
            if root.right == None:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)
        
        elif val < root.val:
            if root.left == None:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left, val)
        
        return root
        