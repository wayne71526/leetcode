# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.left_level, self.right_level = 0, 0
        if not root:
            return 0
        else:
            self.traverse(root)

        return max(self.left_level, self.right_level) + 1

    def traverse(self, node):
        if node.left:
            self.traverse(node.left)
            self.left_level += 1
        
        if node.right:
            self.traverse(node.right)
            self.right_level += 1