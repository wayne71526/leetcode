# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# solution 1
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = 0
        d = {}
        def traverse(node, level):
            if not node:
                return
            if level not in d:
                d[level] = [node.val]
            else:
                d[level].append(node.val)

            level += 1
            traverse(node.left, level)
            traverse(node.right, level)

        traverse(root, level)
        return [d[i] for i in range(len(d))]