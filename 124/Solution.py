```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    current_max = float('-inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dp(root)
        return self.current_max

    def dp(self, root):
        if root == None:
            return 0
        left = self.dp(root.left)
        right = self.dp(root.right)

        if not left or left < 0:
            left = 0
        if not right or right < 0:
            right = 0
        self.current_max = max(left + right + root.val, self.current_max)
        return max(left, right) + root.val 
```