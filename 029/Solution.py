class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign=1
        if dividend*divisor<0:
            sign=-1
        
        count=0
        res=0
        a,b=abs(dividend),abs(divisor)
        if a<b:
            return 0
        
        while a>=b:
            cum=b
            count=1
            while cum+cum<=a:
                cum+=cum
                count+=count
            res+=count
            a-=cum
        
        res=sign*res
        return res if -2**31<=res<=2**31-1 else 2**31-1
        
        
            
        
        
        
    def divide1(self, dividend: int, divisor: int) -> int:
        res=abs(dividend)//abs(divisor)
        if dividend*divisor<0:
            return -res