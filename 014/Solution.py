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
