```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        else:
            list1=[]
            list2=[]
            self.root_recursion(root1,list1)
            self.root_recursion(root2,list2)
            
            if list1==list2:
                return True
            else:
                return False
            
        
    def root_recursion(self,root,list):
        if root==None:
            return
        
        if not root.left and not root.right:
            list.append(root.val)
        
        self.root_recursion(root.left,list)
        self.root_recursion(root.right,list)
```

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        
        def helper(root,list):
            if not root:
                return None
            if not root.left and not root.right:
                list.append(root.val)
            helper(root.left,list)
            helper(root.right,list)
            
            return list
        
        list1=[]
        list2=[]
        helper(root1,list1)
        helper(root2,list2)
        
        if list1==list2:
            return True
        else:
            return False
```