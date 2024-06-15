# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def traverse(node, arr):
            if not node:
                return

            arr.append(node.val)

            if node.left:
                traverse(node.left, arr)

            if node.right:
                traverse(node.right, arr)
        arr = []
        traverse(root, arr)
        arr = sorted(arr)
        ans = math.inf

        for i in range(1, len(arr)):
            ans = min(ans, arr[i] - arr[i-1])

        return ans