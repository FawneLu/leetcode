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