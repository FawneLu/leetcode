- 内置函数
这里可以用一个split函数直接把string按空格拆分成几小块。
```python
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        print s.split()
        return(len(s.split()))
```
