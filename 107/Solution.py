```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res=[]
        if not root:
            return res
        
        queue=collections.deque()
        queue.append(root)
        while queue:
            cur_list=[]
            for i in range(len(queue)):
                node=queue.popleft()
                if node:
                    cur_list.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            res.append(cur_list)
        
        return res[::-1]
```

```python3
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        return self.preorder(root,0,[])
        
    def preorder(self,root,level,res):
        if root:
            if len(res)<level+1:
                res.insert(0,[])
            res[-(level+1)].append(root.val)
            self.preorder(root.left,level+1,res)
            self.preorder(root.right,level+1,res)
        return res
        
        # if root:
        #     if len(res)<level+1:
        #         res.append([])
        #     res[level].append(root.val)
        #     self.preorder(root.left,level+1,res)
        #     self.preorder(root.right,level+1,res)
        # return res[::-1]
```