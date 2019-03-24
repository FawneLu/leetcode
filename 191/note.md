 - Use built-in function Counter  
Counter to count the number of the appearance of the element in the list.  
Key of the dictionary refers to the element;  
Value of the dictionary refers to the number of appearance.   
First , using bin() to change the int to string, then return the value whose key is 1.  
```python
from collections import Counter

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=bin(n)
        print(a)
        num_dict=Counter(a)
        print(num_dict["1"])
```  
- Bit Operation   
AND: When the two numbers are 1, the the result is 1. Otherwise, results are 0.  
We can apply AND operation in this problem, that n=n&(n-1)(in n-1, the least significant 1 in n will change into 0). When n=0, the number of calculation is the number of 1.  
**Best time complexity:O(n); Best sapce complexity O(1)**  
```python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        count=0
        while n!=0:
            n &=n-1
            count+=1
        return count

```