# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.traverse(root.left, root.right)

    def traverse(self, left_node, right_node):
        if left_node == None and right_node == None:
            return True

        if left_node == None or right_node == None:
            return False

        if left_node.val != right_node.val:
            return False

        return self.traverse(left_node.left, right_node.right) and self.traverse(left_node.right, right_node.left)