- 用迭代实现树的中序遍历
这道题就是用一个while循环实现树的中序遍历。我们可以用一个stack来存储树的结果。
```python3
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root:
            return 
        
        def helper(root,res):
            if not root:
                return 
            helper(root.left,res)
            res.append(root.val)
            helper(root.right,res)
            
            return res
        
        return helper(root,[])
```  
这边我自己要注意的是，如果用递归要学会看返回的变量。注意nonlocal的用法。nonlocal用来在函数或其他作用域中使用外层非全局变量。例如：  
```python3
b=20
def func():
	a=10
	def test():
		print(a)
```  
此时，a就是一个非全局变量,b就是全局变量。global可以用来定义全局变量，global的作用是打穿所有作用域。