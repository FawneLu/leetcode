- 又不是我自己想出来的
这题也是看了张老师的，因为这是我的第一个String。我发现string是可以同样操作的。这题先判断一下strs是不是空。然后按长度进行排序。再从第一个开始向后判断有没有相同的字母。
```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if not strs:
            return ""
        strs.sort(key=len)
        max_length = len(strs[0])
        common_prefix = ""
        for i in range(max_length):
            for j in range(len(strs) - 1):
                if strs[j][i] != strs[j + 1][i]:
                    return common_prefix

            common_prefix += strs[0][i]
        return common_prefix
```
