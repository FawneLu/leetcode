- Use built-in function reverse    
Firstly, we can use '{:032b}'.format(n) to change the int to binary, then we change it to the list and use .reverse() to reverse it. FInally we chang it into string and then into int.  
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
- Bit Operation  
Just think about reversing an int(mod and divide).  
Left shift equals multipling the number by 2, right shift equals dividing the number by 2.  
**Best time complexity:O(n); Best sapce complexity O(1)**
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