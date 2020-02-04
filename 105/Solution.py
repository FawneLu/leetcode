```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return 
        
        root=TreeNode(preorder[0])
        index=inorder.index(preorder[0])
        preorder=preorder[1:]
        n=len(inorder[:index])
        root.left=self.buildTree(preorder[:n],inorder[:index])
        root.right=self.buildTree(preorder[n:],inorder[index+1:])
        
        return root
```