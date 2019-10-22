```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        count=0
        def helper(root):
            nonlocal count
            if not root:
                return
            left=helper(root.left)
            right=helper(root.right)
            
            if (not left or left==root.val) and (not right or right==root.val):
                count+=1
                return root.val
            return "#"
        
        helper(root)
        return count
```