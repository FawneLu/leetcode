class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"
        
        res=0
        for i,n2 in enumerate(num2[::-1]):
            cur=0
            pre=0
            for j,n1 in enumerate(num1[::-1]):
                multi=(ord(n1)-ord("0"))*(ord(n2)-ord("0"))
                first,second=multi//10,multi%10
                cur+=(second+pre)*(10**j)
                pre=first
            cur+=pre*(10**len(num1))
            res+=cur*(10**i)
        return str(res)
                
        
        
        
    def multiply1(self, num1: str, num2: str) -> str:
        return str(int(num1)*int(num2))