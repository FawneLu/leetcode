```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val<key:
            root.right=self.deleteNode(root.right,key)
        if root.val>key:
            root.left=self.deleteNode(root.left,key)
        if root.val==key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            if root.left and root.right:
                p=root.right
                while p.left:
                    p=p.left
                root.val=p.val
                root.right=self.deleteNode(root.right,p.val)
                return root
        return root
```
```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val<key:
            root.right=self.deleteNode(root.right,key)
        if root.val>key:
            root.left=self.deleteNode(root.left,key)
        if root.val==key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            if root.left and root.right:
                left=root.left
                right=root.right
                p=right
                while p.left:
                    p=p.left
                p.left=left
                return right
        return root

```