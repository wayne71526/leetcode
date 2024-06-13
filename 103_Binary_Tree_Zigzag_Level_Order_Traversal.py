# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        queue.append(root)
        ans = []

        while queue:
            queue_len = len(queue)
            level = []

            for i in range(queue_len):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
            
                if node.right:
                    queue.append(node.right)

            ans.append(level)
        
        for i in range(len(ans)):
            if i % 2 != 0:
                ans[i].reverse()

        return ans