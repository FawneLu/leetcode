- 简单思路
把二进制的数化成十进制相加再转成二进制。因为这样的结果前面会有”0b“，所以结果的字符串要从第三位开始输出来。
```python
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return str(bin(int(a,2)+int(b,2)))[2:]
```
