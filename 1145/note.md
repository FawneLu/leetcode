### 二叉树遍历
这道题的思路比较清楚，首先我们用一个dfs找出x对应的位置
```python
def dfs(node):
            if not node:
                return
            if node.val==x:
                self.x_address=node
                return 
            dfs(node.left)
            dfs(node.right)
```  
然后计算出x左子树的node 数量x_left,x右子树的节点数量 x_right， x为root的子树的节点数量x_node还有整个树的节点数量total。
```python
def count_node(node):
            if not node:
                return 0
            return 1+count_node(node.left)+count_node(node.right)
```    
要想赢有集中情况：  
1. x为根节点，那左右子树的个数要不相同，如果相同则会输；  
2. 选x的父节点要保证total-x_node>x_node;  
3. 选x的左孩子，那么x_left>total-x_left;  
4. 选x的右孩子，那么x_right>total-x_right。
```python
if self.x_address==root:
            return x_left_count!=x_right_count
        return x_node_count<total-x_node_count or x_left_count>total-x_left_count or x_right_count>total-x_right_count
```