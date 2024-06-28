# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 當 node 和 root 為空時停止
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        left = self.hasPathSum(root.left, targetSum-root.val)
        right = self.hasPathSum(root.right, targetSum-root.val)

        return left or right