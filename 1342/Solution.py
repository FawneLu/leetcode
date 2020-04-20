class Solution:
    def numberOfSteps (self, num: int) -> int:
        binary = bin(num)[2:0]
        count=0
        while num:
            if num & 1:
                count+=2
            else:
                count+=1
            num=num>>1
        return count-1
                
        
    def numberOfSteps1 (self, num: int) -> int:
        count=0
        while num:
            if num%2==0:
                num/=2
            else:
                num-=1
            count+=1
        return count