- 用迭代实现前序遍历  
这道题是用迭代实现前序遍历。我们需要与中序遍历区别。要先打印根节点的值。
```python3
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack=[]
        res=[]
        if not root:
            return res
        
        while stack or root:
            while root:
                res.append(root.val)
                stack.append(root)
                root=root.left
            
            cur_node=stack.pop()
            root=cur_node.right
        return res
```