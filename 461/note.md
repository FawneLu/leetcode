- Bin Manipiulation  
We can use ^ to get the number(position of different number between the two inputs is 1, the same is 0). Then we can use &(n&n-1) to count the number of '1's.  
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