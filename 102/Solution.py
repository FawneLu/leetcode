```python3
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        return self.preorder(root,0,[])
    
    def preorder(self,root,level,res):
        if root:
            if len(res)<level+1:
                res.append([])
            res[level].append(root.val)
            self.preorder(root.left,level+1,res)
            self.preorder(root.right,level+1,res)
            
        return res
```

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res=[]
        if not root:
            return res
        
        q=[root]
        while len(q)!=0:
            res.append([node.val for node in q])
            new_q=[]
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            
                q=new_q
        
        return res
```