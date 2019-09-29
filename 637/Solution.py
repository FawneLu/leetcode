```python3
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        if not root:
            return []
        queue=deque([(root,0)])
        level=0
        table={}
        while queue:
            cur,level=queue.popleft()
            if level not in table:
                table[level]=[cur.val]
            else:
                table[level].append(cur.val)
            
            if cur.left:
                queue.append((cur.left,level+1))
            if cur.right:
                queue.append((cur.right,level+1))
                
        return [sum(table[i])/len(table[i]) for i in range(len(table))]
        
```