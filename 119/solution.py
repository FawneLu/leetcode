```python
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res=[]
        for i in range(rowIndex+1):
            res.append([1]*(i+1))
            for j in range(1,i):
                res[i][j]=res[i-1][j-1]+res[i-1][j]
        return res[rowIndex]
 ```
