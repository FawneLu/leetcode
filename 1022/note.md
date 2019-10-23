- 哭了，我发现自己还是不怎么会写递归
我自己想的思路大概是对的，但是还是不是很会想。大概就是，有一个空的string，然后每一次都加上节点的值，到了叶子节点之后就append到空的数组里。  
最后写个循环，把数组里的string转化为十进制然后把值加起来。  
注意，如果只有根节点，直接返回根节点的值就好，因为此时数组为空。
```python3
def helper(root,num):
            nonlocal number
            if not root:
                return
            
            if not root.left and not root.right:
                number.append(num+str(root.val))
                return
            
            helper(root.left,num+str(root.val))
            helper(root.right,num+str(root.val))
            
            return number
```