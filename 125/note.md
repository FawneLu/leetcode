- 简单方法
这道题最捞的一个方法就是先把字符串里的特殊符号全都去掉，然后转化为小写，这边用”“.join(re.split("\W+",string)),这边注意join函数和split函数的用法。然后再把这个string反转一下进行比较。
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
