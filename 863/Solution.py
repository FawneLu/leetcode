```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        graph=collections.defaultdict(set)
        def connect(parent,child):
            if parent and child:
                graph[parent.val].add(child.val)
                graph[child.val].add(parent.val)
            if child.left:
                connect(child,child.left)
            if child.right:
                connect(child,child.right)
        connect(None,root)
        
        queue = collections.deque() 
        queue.append(target.val)
        visited = set()
        visited.add(target.val)
        for _ in range(K):
            for _ in range(len(queue)):
                node=queue.popleft()
                for i in graph[node]:
                    if i not in visited:
                        queue.append(i)
                        visited.add(i)
                        
        return list(queue)
```