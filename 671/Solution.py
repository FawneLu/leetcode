```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        
        result=[]
        
        def get_value(root,result):
            if not root:
                return
            
            else:
                result.append(root.val)
                get_value(root.left,result)
                get_value(root.right,result)
                
        get_value(root,result)
        nodes=set(result)
        if len(nodes)<=1:
            return -1
        else:
            return sorted(list(nodes))[1]
        
        # def find_second(nodes):
        #     diff_nodes = set(nodes)
        #     if len(diff_nodes) <=1:
        #         return -1
        #     else:
        #         return sorted(list(diff_nodes))[1]
        
        #return find_second(result)
```
```python3
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        
        queue=deque()
        queue.append(root)
        
        min_val=root.val
        second_min=float('inf')
        found=False
        
        while queue:
            cur=queue.popleft()
            if cur.val>min_val and cur.val<second_min:
                second_min=cur.val
                found=True
                continue
            if not cur.left:
                continue
                
            queue.append(cur.left)
            queue.append(cur.right)
        
        return second_min if found else -1
```
```python3
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        
        min_val=root.val
        
        def DFS(root,min_val):
            if not root:
                return -1
            
            if root.val>min_val:
                return root.val
            
            min_l=DFS(root.left,min_val)
            min_r=DFS(root.right,min_val)
            
            if min_l==-1:
                return min_r
            if min_r==-1:
                return min_l
            
            return min(min_l,min_r)
        
        return DFS(root,min_val)
```