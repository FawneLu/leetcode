- 树好难，我又哭了
同样这道题可以用BFS和DFS两种思路。  
1. BFS,同样层序遍历，最后我们输出res[::-1]即可。注意层序遍历要用queue。先把根节点append再pop，再append左右子树。
```python3
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
2. 用DFS,和之前一题的想法类似。但是我们每次都在res的最前面insert一个[]，而且要倒着插值，res[-(level+1)].append(root.val)。
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