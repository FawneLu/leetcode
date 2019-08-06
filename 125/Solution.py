```python
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # for i in s:
        #     if i==',' or i==' ' or i==':' or i=='.':
        
        s="".join(re.split("\W+",s.lower()))
        #print s
        return s==s[::-1]
```

