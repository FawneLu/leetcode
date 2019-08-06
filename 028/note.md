- 终于自己写了一道题
耶，这道题是我自己写出来的。虽然用了很长时间，但是我还是写出来了。这题的思路是这样。先判断needle的第一个字母在不在haystack里面，如果在的话就继续比较needle剩下的字母和haystack的字母是否相等。如果相等就返回index，不相等返回-1。循环嵌套。
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
- 感觉很牛逼的方法
是我太蠢了，python里string是可以直接比较的，不用一个字符一个字符的去看......
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
