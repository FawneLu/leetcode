- 我已经不会思考了
这道题首先第一个思路是，把所有的节点的值append到一个list中，再判断是否存在第二大的节点，如果不存在就返回-1。  
```python3
def get_value(root,result):
            if not root:
                return
            
            else:
                result.append(root.val)
                get_value(root.left,result)
                get_value(root.right,result)
```
判断时候存在第二大的节点也可以写一个函数。
```python3
def find_second(nodes):
            diff_nodes = set(nodes)
            if len(diff_nodes) <=1:
                return -1
            else:
                return sorted(list(diff_nodes))[1]
```
