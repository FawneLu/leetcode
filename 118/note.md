- 这里用了一个比较巧的思路，因为每一行的首尾都是1，所以每次先把所有的res每一行的所有数比变成1，再把要改的对应位置的数变为前一行的和。
```python
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res=[]
        for i in range(0,numRows):
            res.append([1]*(i+1))
            for j in range(1,i):
                res[i][j]=res[i-1][j-1]+res[i-1][j]
        return res
```  
