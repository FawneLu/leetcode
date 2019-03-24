 - Use built-in function Counter  
Firstly, we need to judge whether the input is above 0 or below 0. If it is less than 0, then the input is not the power of two. If it is larger or equal 0, then we use Counter to count the number of 1 and 0. If the number of 1 is 1, then the input is the power of 2.  
**This one is bad!!! Terribly bad**
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
Or, we can just use count.  
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
- AND:When the two numbers are 1, the the result is 1. Otherwise, results are 0.  
We apply this way in the problem, if we do the and operation between n and n-1 then the result must be 0 if the input is power of 2. Otherwise return false.  
**Best time complexity:O(1); Best sapce complexity O(1)**  
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