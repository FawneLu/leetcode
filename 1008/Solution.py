```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return
        
        def helper(root,item):
            if not root:
                return
            
            if not root.left and root.val>item:
                root.left=TreeNode(item)
            if not root.right and root.val<item:
                root.right=TreeNode(item)
                
            if root.val>item:
                helper(root.left,item)
            else:
                helper(root.right,item)
            
        preorder=preorder[::-1]
        
        root=TreeNode(preorder.pop())
        
        while preorder:
            item=preorder.pop()
            helper(root,item)
        
        return root
```