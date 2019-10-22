- 树好难啊，我枯了
这道题有两个思路。一个是用DFS,一个是用BFS。
1. DFS的思想是这是一个先序遍历，我们同时可以用一个level来存储每层的值。  
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
2. BFS的想法是，我们用一个queue存储你每一层的节点。把这层节点的值append进list。每判断一次就用一个new_q存储左右节点，再把q置为new_q。
```python3
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