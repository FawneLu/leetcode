```python
class Solution(object):
    def Counter(self,num):
        count=0
        while num:
            num &=num-1
            count+=1
        return count
    
    def Prime(self,p):
        if p==1:
            return False
        for i in range(2,int(p**0.5)+1):
            if p%i==0:
                return False
        return True
    
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        result=0
        for n in range(L,R+1):
            num_bit=self.Counter(n)
            if self.Prime(num_bit):
                result+=1
        return result
``` 