- 我已经不会思考了
1. 这道题首先第一个思路是，把所有的节点的值append到一个list中，再判断是否存在第二大的节点，如果不存在就返回-1。  
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
2. 这道题的第二种解思路是广度优先搜索。我们用一个deque。首先将第二小的值设为无穷大。  
广度优先搜索遍历整棵树。当前节点的值大于最小值小于第二小的值是，将第二小的值置为当前节点的值。  
当前节点不存在左右孩子时，孩子节点不用入栈（只考虑左子树即可）。  
将该节点的左右孩子append进队列。  
```python3
if not root:
            return -1
        
        queue=deque()
        queue.append(root)
        
        min_val=root.val
        second_min=float('inf')
        found=False
        
        while queue:
            cur=queue.popleft()
            if cur.val>min_val and cur.val<second_min:
                second_min=cur.val
                found=True
                continue
            if not cur.left:
                continue
                
            queue.append(cur.left)
            queue.append(cur.right)
        
        return second_min if found else -1
```  
3. 这道题的第三种解思路是用深度优先搜索。  
每一个根节点的值都为左右子树的最小值。对当前根节点而言，如果左孩子节点的值大于最小值，返回当前值，不存在则返回-1。如果左孩子节点的值等于根节点的值就递归调用左子树。右孩子节点同理。  
```python3
if not root:
            return -1
        
        min_val=root.val
        
        def DFS(root,min_val):
            if not root:
                return -1
            
            if root.val>min_val:
                return root.val
            
            min_l=DFS(root.left,min_val)
            min_r=DFS(root.right,min_val)
            
            if min_l==-1:
                return min_r
            if min_r==-1:
                return min_l
            
            return min(min_l,min_r)
        
        return DFS(root,min_val)
```

