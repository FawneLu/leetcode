```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res=[]
        node_queue=collections.deque([root,None])
        level_queue=collections.deque()
        orderleft=True
        
        while node_queue:
            current=node_queue.popleft()
            if current:
                if orderleft:
                    level_queue.append(current.val)
                else:
                    level_queue.appendleft(current.val)
                
                if current.left:
                    node_queue.append(current.left)
                if current.right:
                    node_queue.append(current.right)
            
            else:
                res.append(level_queue)
                if node_queue:
                    node_queue.append(None)
                level_queue=collections.deque()
                orderleft=not orderleft
                
        return res
```