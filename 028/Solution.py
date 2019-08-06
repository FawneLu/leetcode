```python
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        index=-1
        if not needle and not haystack:
            return 0
        if not needle and haystack:
            return 0
        if needle and not haystack:
            return index
        if len(needle)>len(haystack):
            return index
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i]==needle[0]:
                index=i
                j=0
                for i in range(index,index+len(needle)):
                    if haystack[i]==needle[j]:
                        j+=1
                        if j==len(needle):
                            return index
                    else:
                        break
        return -1
```
```python
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
         if not needle:
            return 0
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1
```
