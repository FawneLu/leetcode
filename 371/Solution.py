```python  
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
        return (sum([a,b]))
```  
```python
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b:
            tmp = a & b
            a = a ^ b
            b = tmp << 1
        return a
```