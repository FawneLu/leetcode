- 迭代实现后序遍历
这道题是用迭代实现后序遍历。我们可以用一个last_visit来判断当前节点的右节点是不是访问过。是的话就pop这个节点，不是的话就将root置为当前节点的右节点。
```python3
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:  
        res=[]
        stack=[]
        last_visit=None
        if not root:
            return res
        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            
            cur_node=stack[-1]
            if not cur_node.right or cur_node.right==last_visit:
                item=stack.pop()
                res.append(item.val)
                last_visit=item
            
            elif cur_node.right:
                root=cur_node.right
        
        return res
```
