```python
class Solution(object):
    def Count(self,num):
        count=0
        while num:
            num &=num-1
            count+=1
        return count
    
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return self.Count(x^y)
```  