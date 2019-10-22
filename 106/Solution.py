```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return
        index=inorder.index(postorder.pop())
        root=TreeNode(inorder[index])
        root.right=self.buildTree(inorder[index+1:],postorder)
        root.left=self.buildTree(inorder[:index],postorder)
        
        return root
```