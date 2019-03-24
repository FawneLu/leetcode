 The difference between this problem and the 'power of two' is that in the binary, the 1 must be on the odd position.  

- Normal Way  
Firstly, we use bin operation to judge whether there's only one '1' in the binary and then we judge whether the odd position is '1'.  
```python
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if(num>0 and (num&(num-1))==0 ):
            n = '{:032b}'.format(num)
            l=list(n)
            #print(l)
            for i in range(len(l)):
                #print(i)
                if(i%2==1 and l[i]=="1"):
                    return True
        else: return False

```  
- Tricky Mask  
We can use AND operation betwwen '0b01010101010101010101010101010101' and input to judge whether the only 1 is on the odd position(num& 0b01010101010101010101010101010101==num).  
**Best time complexity:O(1); Best sapce complexity O(1)**
```python
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return (num>0 and (num&(num-1))==0 and (num&0b01010101010101010101010101010101==num))
```  