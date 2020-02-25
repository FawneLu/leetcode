```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return root
        queue=collections.deque()
        queue.append((root,0,0))
        m_=list()
        while queue:
            node,x,y=queue.popleft()
            m_.append((x,-y,node.val)) 
            if node.left:
                queue.append((node.left,x-1,y-1))
            if node.right:
                queue.append((node.right,x+1,y-1))
        m_=sorted(m_,key=lambda x:(x[0],x[1]))
        res=[[m_[0][2]]]
        for i in range(1,len(m_)):
            if m_[i][0]==m_[i-1][0]:
                res[-1].append(m_[i][2])
            else:
                res.append([m_[i][2]])
        
        return res
```