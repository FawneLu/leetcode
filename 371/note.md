- use sum  
```python  
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
        return (sum([a,b]))
```  
- Bin Operation  
我们用异或去计算两个数的模2加，用两个数的与，右移1位来表示他们的进位。这两个位运算的数相加即是两数之和。 python 用来实现这种方法不现实，因为会不停地进位，循环就不会暂停。用C语言或者C++可以实现。
```python
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b:
            tmp = a & b
            a = a ^ b
            b = tmp << 1
        return a
```