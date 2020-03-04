```python
class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        graph=collections.defaultdict(list)
        leaves=set()
        def traverse(node):
            if not node:
                return
            if not node.left and not node.right:
                leaves.add(node.val)
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                traverse(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                traverse(node.right)
        traverse(root)
        print(graph)
        queue=collections.deque([k])
        visited=set()
        visited.add(k)
        while queue:
            node=queue.popleft()
            if node in leaves:
                return node
            for n in graph[node]:
                if n not in visited:
                    visited.add(n)
                    queue.append(n)
```