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
