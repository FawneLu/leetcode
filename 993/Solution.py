```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        
        fathers=[]
        levels=[]
        queue=collections.deque([(None,0,root)])
        while queue:
            father,level,root=queue.popleft()
            if root.val==x or root.val==y:
                fathers.append(father)
                levels.append(level)
            if root.left:
                queue.append((root,level+1,root.left))
            if root.right:
                queue.append((root,level+1,root.right))
        
        if fathers[1]!=fathers[0] and levels[1]==levels[0]:
            return True
        else:
            return False
```