- 自己有思路但是不会写
这道题的思路其实还挺简单，理解题目就是先找list里最大的数为根节点。然后这个数把list分为左右两个sublist，再利用左右这两个sublist构建左右两个subtree。简单的递归。注意要会用list的表示方法。[0:index],[index+1:]。同时要注意递归返回的是根节点。  
```python3
def construct(nums):
            if not nums:
                return
            
            max_num,index=find_max(nums)
            root=TreeNode(max_num)
            root.left=construct(nums[0:index])
            root.right=construct(nums[index+1:])
            
            return root
```