# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if self.traverse(root) == False:
            return False
        else:
            return True


    def traverse(self, node, min_val=float('-inf'), max_val=float('inf')):
        if not node:
            return True

        if node.val <= min_val or node.val >= max_val:
            return False

        return self.traverse(node.left, min_val, node.val) and self.traverse(node.right, node.val, max_val)