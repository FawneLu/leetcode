```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:  
         nums_dict = {}  
         for num in nums:  
             if num not in nums_dict:  
                 nums_dict[num] = 1  
             else:  
                 nums_dict[num] += 1  
```  
```python
from collections import Counter  

class Solution:  
    def singleNumber(self, nums: List[int]) -> int:  
         nums_dict = Counter(nums)  
         for key,value in nums_dict.items():  
             if value == 1:  
                 return key  
```
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
         ini = 0
         for num in nums:
             ini ^= num
         return ini
```python
from operator import xor
from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
         return reduce(xor,nums)
```