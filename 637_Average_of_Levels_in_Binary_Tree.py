# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        d = {}

        def traverse(node, level):
            if not node:
                return

            if level not in d:
                d[level] = [node.val, 1]  # [node_sum, node_count] for the same level
            else:
                d[level][0] += node.val
                d[level][1] += 1
            
            level += 1
            traverse(node.left, level)
            traverse(node.right, level)

        traverse(root, 0)
        ans = []
        for i in range(len(d)):
            ans.append(d[i][0] / d[i][1])

        return ans