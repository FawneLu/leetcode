- 我是臭弟弟
这道题可以用层序遍历。找到需要的节点x,y之后，就记录对应的父节点和level，最后比较两者是否相等。  
如果是层序遍历，我们都可以用一个queue解决，准确地说，可以用一个deque来解决。把每一层append进去，再popleft。
```python3
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