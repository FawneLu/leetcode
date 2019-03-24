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
```python
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return (num>0 and (num&(num-1))==0 and (num&0b01010101010101010101010101010101==num))
```  