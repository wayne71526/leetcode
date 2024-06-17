# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        value = []
        self.traverse(root, value)
        value = sorted(value)

        return value[k-1]

    def traverse(self, node, value):
        if not node:
            return
        
        value.append(node.val)

        if node.left:
            self.traverse(node.left, value)

        if node.right:
            self.traverse(node.right, value)