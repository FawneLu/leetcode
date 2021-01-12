# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        queue = collections.deque()
        queue.append(root)
        res = []
        
        while queue:
            size = len(queue)
            max_ = float('-inf')
            
            for _ in range(size):
                node = queue.popleft()
                max_ = max(max_, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(max_)
        
        
        return res
                