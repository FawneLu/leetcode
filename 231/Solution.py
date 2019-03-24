```python
from collections import Counter
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n>0):
            a=bin(n)
            num_dict=Counter(a)
            if(num_dict["1"]==1):
                return 1
            else:
                return 0
        else: 
            return 0
```  
```python
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n<=0):
            return False
        else:
            return bin(n).count('1')==1
```  
```python
from collections import Counter
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and (n&(n-1))==0
```  