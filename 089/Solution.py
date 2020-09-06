class Solution:
    def grayCode(self, n: int) -> List[int]:
        return map(lambda x:int(x,2),self.bit_gray(n))
    
    def bit_gray(self,n):
        ans = None
        if n == 0:
            ans = ["0"]
        elif n == 1:
            ans = ["0", "1"]
        else:
            pre_gray = self.bit_gray(n-1)
            ans = ["0" + x for x in pre_gray] + ["1" + x for x in pre_gray[::-1]]
        return ans
            
            
        
        
        
    def grayCode1(self, n: int) -> List[int]:
        grays = dict()
        grays[0] = ["0"]
        grays[1] = ["0", "1"]
        for i in range(2, n+1):
            n_gray = []
            for pre in grays[i-1]:
                n_gray.append("0" + pre)
            for pre in grays[i-1][::-1]:
                n_gray.append("1" + pre)
            
            grays[i] = n_gray
        
        return map(lambda x:int(x,2),grays[n])