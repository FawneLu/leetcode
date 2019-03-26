- Silly Way  
Firstly, we can convert the list to the string and then to int. Then we make the int plus one and convert it back to list. 
```python
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a=map(str, digits)
        a=str(int("".join(a))+1)
        res=map(int,list(a))
        return res
```
