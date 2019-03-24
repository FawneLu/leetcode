- Normal Way  
Create a new Dictionary, if element in the list exists(in the form of key) in the dictionary, then the value will add 1.  
If the the element doesn't have a corresponding key, then the value equals to 1.  
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

- Use built-in function Counter  
Counter to count the number of the appearance of the element in the list.  
Key of the dictionary refers to the element;  
Value of the dictionary refers to the number of appearance.  
```python
from collections import Counter  

class Solution:  
    def singleNumber(self, nums: List[int]) -> int:  
         nums_dict = Counter(nums)  
         for key,value in nums_dict.items():  
             if value == 1:  
                 return key  
```

- Bit Operation  
XOR: If the 2 numbers are the same, then the result is 0. 0 and any other number do the XOR operation, the result is that number. So we can apply XOR operation in this problem.  The result of the XOR operation in this problem is the number which appear once.  
**Best time complexity:O(n); Best sapce complexity O(1)**  
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
         ini = 0
         for num in nums:
             ini ^= num
         return ini
```
We can also use built-in operator 'xor' and built-in functool 'reduce'.  
```python
from operator import xor
from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
         return reduce(xor,nums)
```