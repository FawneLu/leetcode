```python
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        #print(type(n))
        num = '{:032b}'.format(n)
        #print(num)
        l=list(num)
        l.reverse()
        b="".join(l)
        #print(type(b))
        b=int(b,2)
        return b
```  

```python
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        result=0
        for i in range(32):
            result=(result<<1)+n%2
            n=n>>1
        return result
```