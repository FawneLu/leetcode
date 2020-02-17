```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.m_ = list()
        self.dfs(root, 0, 0)
        self.m_.sort()
        res = [[self.m_[0][2]]]
        for i in range(1, len(self.m_)):
            if self.m_[i][0] == self.m_[i - 1][0]:
                res[-1].append(self.m_[i][2])
            else:
                res.append([self.m_[i][2]])
        return res
        
    def dfs(self, root, x, y):
        if not root: return
        self.m_.append((x, -y, root.val))
        self.dfs(root.left, x - 1, y - 1)
        self.dfs(root.right, x + 1, y - 1)

        
        
        
    def verticalTraversal1(self, root: TreeNode) -> List[List[int]]:
        q = collections.deque()
        q.append((root, 0, 0))
        m_ = list()
        while q:
            node, x, y = q.popleft()
            m_.append((x, -y, node.val))
            if node.left:
                q.append((node.left, x - 1, y - 1))
            if node.right:
                q.append((node.right, x + 1, y - 1))
        m_.sort()
        res = [[m_[0][2]]]
        for i in range(1, len(m_)):
            if m_[i][0] == m_[i - 1][0]:
                res[-1].append(m_[i][2])
            else:
                res.append([m_[i][2]])
        return res
```