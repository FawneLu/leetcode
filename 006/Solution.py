class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        
        res=""
        interval=2*(numRows-1)
        for i in range(0,len(s),interval):
            res+=s[i]
        
        for row in range(1,numRows-1):
            inter=2*row
            i=row
            while i<len(s):
                res+=s[i]
                inter=interval-inter
                i+=inter
        
        for i in range(numRows-1,len(s),interval):
            res+=s[i]
        
        return res