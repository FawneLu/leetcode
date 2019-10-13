```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy=cur=TreeNode(None)
        
        def inordertree(root):
            nonlocal cur
            if root:
                inordertree(root.left)
                root.left=None
                cur.right=root
                cur=cur.right
                inordertree(root.right)
        
        inordertree(root)
        return dummy.right
```