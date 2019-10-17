- 这道题好难啊我又枯了
这道题用了一个笛卡尔积。我们知道n=1的时候有1种方法，n=3的时候有1种方法。当n为5的时候，1可以在左边，3可以在右边，这时的可能性是1x1，1种。同时也可以1在右边，3在左边，这时的可能性也是1X1，1种。总共的可能性一共是1+1两种。  
当n为7的时候，我们的可能性是{1,5}{5,1}{3,3},总共的可能性是1X2+2X1+1X1=5，一共5种。
```python3
class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        # if N%2==0:
        #     return []
        if N==1:
            return[TreeNode(0)]
        res=[]
        for l in range(1,N,2):
            for left in self.allPossibleFBT(l):
                for right in self.allPossibleFBT(N-l-1):
                    root=TreeNode(0)
                    root.left=left
                    root.right=right
                    res.append(root)
        
        return res
```